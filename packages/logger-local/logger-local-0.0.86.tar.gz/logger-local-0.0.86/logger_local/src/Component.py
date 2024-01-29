from python_sdk_remote.mini_logger import MiniLogger

from .Connector import get_connection

cache = {}


class Component:
    @staticmethod
    def getDetailsByComponentId(component_id: int | str) -> tuple[str, str, str, str, str] | None:
        if component_id in cache:
            return cache[component_id]
        try:
            connection = get_connection(schema_name="component")
            cursor = connection.cursor()
            sql_query = ("SELECT name, component_type, component_category, testing_framework, api_type "
                         "FROM component.component_table WHERE component_id = %s")
            cursor.execute(sql_query, (component_id,))
            result = cursor.fetchone()
            cache[component_id] = result
            return result
        except Exception as e:
            MiniLogger.exception("getDetailsByComponentId Exception: " + str(e))
