import json
import re
from tempfile import NamedTemporaryFile
from typing import List, Dict

import sqlparse

SOURCE_FORMAT_EXTENSION = {
    'CSV': '.csv',
    'TSV': '.tsv',
    'JSON_NEWLINE': '.json'
}


class FeedService:
    def __init__(self, app):
        """
        :type app: metasdk.MetaApp
        """
        self.__app = app
        self.__options = {}
        self.__data_get_cache = {}
        self.__data_get_flatten_cache = {}
        self.__metadb = app.db("meta")
        self.__media = app.MediaService
        self.__starter = app.StarterService

    def get_feed(self, datasource_id):
        """
        Получение настроек для фида
        :param datasource_id: идентификатор фида
        :return: FeedDataSource
        """
        info = self.__metadb.one(
            """
            SELECT to_json(ds) as datasource
                 , to_json(fc) as connector
                 , to_json(fct) as connector_type
                 , to_json(ctp) as connector_type_preset
                 , json_build_object('email', u.email, 'full_name', u.full_name) as author_user
                 , json_build_object('id', fst.id, 'alias', fst.alias) as share_type
              FROM meta.feed_datasource ds
              LEFT JOIN meta.feed_connector fc 
                     ON fc.id=ds.connector_id
              LEFT JOIN meta.feed_connector_type fct 
                     ON fct.id=fc.connector_type_id
              LEFT JOIN meta.feed_connector_type_preset ctp 
                     ON ctp.id=ds.connector_type_preset_id
              LEFT JOIN meta.user_list u 
                     ON u.id=ds.author_user_id
              LEFT JOIN meta.feed_share_type fst 
                     ON fst.id = ds.share_type_id
             WHERE ds.id = :datasource_id::uuid
            """,
            {"datasource_id": datasource_id}
        )
        return FeedDataSource(**info)

    def get_data(self, datasource, callback):
        """
        Сохранение медиафайла
        :param task:
        :param media_metadata:
        :param file_suffix:
        :param callback:
        :return:
        """
        task = self.__app.worker.current_task
        media_metadata = datasource.connector_type_preset['preset_data']['media_metadata']
        result_data = task['result_data']
        tmp_file = NamedTemporaryFile(delete=False, suffix=SOURCE_FORMAT_EXTENSION.get(media_metadata['sourceFormat']))
        self.__app.log.info("Открываем файл", {"filename": tmp_file.name})
        with open(tmp_file.name, 'wb') as f:
            callback(f)

        self.__app.log.info("start media upload")

        result_data['stage_id'] = "persist_media_file"
        self.__starter.update_task_result_data(task)
        result = self.__media.upload(open(tmp_file.name), {
            "ttlInSec": 60 * 60 * 24,  # 24h
            "entityId": 2770,
            "objectId": task.get('data', {}).get("ds_id"),
            "info": {"metadata": media_metadata}
        })

        result_data['stage_id'] = "generate_media_finish"
        result_data['media_id'] = result['id']
        self.__starter.update_task_result_data(task)

        return result

    def datasource_process(self, datasource_id):
        """
        deprecated
        Запускает настроенные обработки в фиде
        :param datasource_id: uuid
        """
        # TODO Выпилить потом класс используется для другого
        # TODO без applicationId не выбираются поля сущностей. Подумать на сколько это НЕ нормально
        response = self.__app.native_api_call('feed', 'datasource/' + datasource_id + '/process?applicationId=1', {},
                                              self.__options, False, None, False, http_method="POST")
        return json.loads(response.text)

    def list_feeds(self, author_user_id: int, filters: Dict) -> List[Dict]:
        """
        Получает список фидов юзера.

        :param author_user_id: ID юзера, создавшего фид.
        :param filters: поля для фильтрации запроса. Формат '{column_name: filter_value}'.
        :return: список фидов.
        """
        if not author_user_id:
            raise ValueError("'author_user_id' обязательный параметр")

        if not isinstance(filters, dict):
            msg = "filters должен быть словарём, в котором key - это название столбца, а value значение фильтрации"
            raise TypeError(msg)

        query = self.generate_list_feeds_query(filters=filters)
        query_params = {"author_user_id": author_user_id, **filters}
        feeds = self.__metadb.all(query, query_params)
        return feeds

    def generate_list_feeds_query(self, filters: Dict = None) -> str:
        """
        Генерирует SQL запрос для получения списка фидов.

        :param filters: поля для фильтрации запроса. Формат '{column_name: filter_value}'.
        :return: SQL запрос.
        """
        base_query = """
        SELECT
            id,
            name,
            user_status,
            state,
            last_launch_time,
            is_automated,
            tags
        FROM meta.feed_datasource
        WHERE author_user_id = :author_user_id::int8
        """
        filters_query = self.generate_filters_query(filters=filters)
        final_query = f"{base_query} {filters_query}"
        return sqlparse.format(final_query, reindent=True)

    def generate_tags_query(self, tags: List[str]) -> str:
        """
        Гененрирует SQL запрос для фильтрации по полю tags.

        :param tags: список тэгов фида.
        :return: часть SQL запроса с фильтрацией по тэгам.
        """
        if not isinstance(tags, list):
            raise TypeError("tags должен иметь тип List[str]")

        if not tags:
            raise ValueError("tags не может быть пустым")

        tags_expr = []
        for tag in tags:
            # обработка спец символов
            tag_escaped = re.escape(tag)
            tag = f"""tags @> array['{tag_escaped}']"""
            tags_expr.append(tag)
        return " OR ".join(tags_expr)

    def generate_filters_query(self, filters: Dict = None) -> str:
        """
        Гененирует SQL запрос со значениями фильтров.

        :param filters: поля для фильтрации запроса. Формат '{column_name: filter_value}'.
        :return: часть SQL запроса с фильтрами для вставки в WHERE.
        """
        if not filters:
            return ""

        special_types = {
            "state": "meta.feed_datasource_state_type",
            "user_status": "meta.user_status_type",
        }
        filters_sql = []
        for key, value in filters.items():
            if key == "tags":
                tags = self.generate_tags_query(tags=value)
                filter_expr = f"AND {tags}"
            else:
                if special_types.get(key):
                    filter_expr = f"AND {key} = :{key}::{special_types[key]}"
                else:
                    filter_expr = f"AND {key} = :{key}"
            filters_sql.append(filter_expr)
        return " ".join(filters_sql)

    def get_feed_by_id(self, author_user_id: int, feed_id: str, last_tasks: bool = False) -> Dict:
        """
        Получает данные о конкретном фиде.

        :param author_user_id: ID юзера, создавшего фид.
        :param feed_id: ID фида.
        :param last_tasks: если True, то возвращает ID последних тасков фида в поле last_tasks.
        :return: данные о фиде.
        """
        if not author_user_id or not feed_id:
            raise ValueError("'author_user_id' и 'feed_id' обязательные параметры.")

        query = self.generate_feed_by_id_query(last_tasks=last_tasks)
        query_params = {"author_user_id": author_user_id, "feed_id": feed_id}
        feed = self.__metadb.one(query, query_params)
        return feed

    def generate_feed_by_id_query(self, last_tasks: bool = False) -> str:
        """
        Генерирует SQL запрос для получения данных о фиде.

        Запрос дополнитено фильтруется по author_user_id, а не только по feed_id,
        чтобы ограничить доступ юзеров не к своим фидам.

        Для получения списка последних тасков дополнительно обращается к таблице 'job.task'.
        :param last_tasks: если True, то возвращает ID последних тасков фида в поле last_tasks.
        :return: SQL запрос для получения данных о фиде.
        """
        base_feed_columns = [
            "id", "name", "user_status", "state", "last_launch_time", "is_automated", "tags",
            "creation_time", "modification_time", "author_user_id", "last_user_id", "schedules",
            "connector_type_id", "connector_settings_form_data", "connector_type_preset_id",
            "share_type_id", "share_settings_form_data", "parent_id", "billing_client_id", "feed_data",
        ]
        base_feed_cols_query = [f"fd.{col}" for col in base_feed_columns]
        base_feed_cols_query = ", ".join(base_feed_cols_query)
        base_query = f"""
        SELECT
            {base_feed_cols_query},
            fct.name as connector_type_name,
            ctp.name as connector_type_preset_name,
            fst.name as share_type_name
        FROM meta.feed_datasource fd
        LEFT JOIN meta.feed_connector_type fct ON fct.id=fd.connector_type_id
        LEFT JOIN meta.feed_share_type fst ON fst.id = fd.share_type_id
        LEFT JOIN meta.feed_connector_type_preset ctp ON ctp.id = fd.connector_type_preset_id
        WHERE fd.author_user_id = :author_user_id::int8 AND fd.id = :feed_id::uuid
        """
        if last_tasks:
            last_tasks_query = self.generate_last_tasks_query()
            base_query = f"""
            WITH feed_data AS (
            {base_query}
            ),
            {last_tasks_query}
            SELECT
                {base_feed_cols_query},
                fd.connector_type_name,
                fd.connector_type_preset_name,
                fd.share_type_name,
                aggt.last_tasks
            FROM feed_data fd
            LEFT JOIN agg_tasks aggt ON aggt.ds_id = fd.id
            """
        return sqlparse.format(base_query, reindent=True)

    def generate_last_tasks_query(self) -> str:
        """
        Генерирет SQL запрос для получения последних тасков фида.

        Таски сортируются по 'creation_time'.
        Кол-во возвращаемых тасков регулируется переменной 'n_last_tasks'.
        :param feed_id: ID фида.
        :return: часть SQL запроса для получения последних тасков фида
        """
        n_last_tasks = 2
        base_query = f"""
        last_tasks AS (
           SELECT 
             id, 
             ("data" ->> 'ds_id')::uuid as ds_id 
           FROM job.task
           WHERE "service_id" = 'meta.datasource_share' AND "data" ->> 'ds_id' = :feed_id::text
           ORDER BY creation_time desc
           LIMIT {n_last_tasks}
        ), agg_tasks AS (
            SELECT array_agg(id) AS last_tasks, ds_id FROM last_tasks GROUP BY ds_id
        )
        """
        return sqlparse.format(base_query, reindent=True)

    def get_tasks(self, feed_id: str) -> List[Dict]:
        """
        Получает список тасков фида.

        :param feed_id: ID фида.
        :return: данные о таске. '{id: status}'
        """
        if not feed_id:
            raise ValueError("'feed_id' обязательный параметр")

        query = self.generate_tasks_query()
        return self.__metadb.all(query, {"feed_id": feed_id})

    def generate_tasks_query(self) -> str:
        """
        Генерирует SQL запрос для получения списка фидов.

        Таблица 'job.task' переодически очищается, поэтому там будут таски только за последние несколько дней.
        Фильтрация по 'service_id' ускоряет запрос.
        :return: SQL запрос для получения списка тасков фида.
        """
        base_query = """
        SELECT id, status FROM job.task
        WHERE service_id = 'meta.datasource_share' AND data->>'ds_id' = :feed_id::text
        """
        return sqlparse.format(base_query, reindent=True)


class FeedDataSource:
    """
    Класс хранения данных по коннектору
    """

    def __init__(
            self, datasource, author_user, connector,
            connector_type, connector_type_preset,
            share_type,
    ):
        self.datasource = datasource
        self.author_user = author_user
        self.connector = connector
        self.connector_type = connector_type
        self.connector_type_preset = connector_type_preset
        self.share_type = share_type
