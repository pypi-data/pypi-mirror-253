from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerLocal import Logger

from .constants import api_management_local_python_code

logger = Logger.create_logger(object=api_management_local_python_code)


class APILimitsLocal(GenericCRUD):
    def __init__(self) -> None:
        super().__init__(default_schema_name="api_limit", default_table_name="api_limit_table",
                         default_view_table_name="api_limit_view")

    def get_api_limit_tuple_by_api_type_id_external_user_id(self, api_type_id: int, external_user_id: int) -> tuple:
        # TODO: if not external_user_id, get default from api_type_user_external.api_type_user_external_table
        logger.start(object={'api_type_id': api_type_id, 'external_user_id': external_user_id})
        try:
            select_clause = "soft_limit_value,soft_limit_unit,hard_limit_value,hard_limit_unit"
            where = "api_type_id = %s AND external_user_id " + ("IS NULL" if external_user_id is None else "= %s")
            params = (api_type_id, external_user_id) if external_user_id is not None else (api_type_id,)
            api_limit_result = self.select_one_tuple_by_where(
                view_table_name="api_limit_view", select_clause_value=select_clause, where=where, params=params)
            if not api_limit_result:
                raise Exception(f"no api_limit found for "
                                f"api_type_id={api_type_id} and external_user_id={external_user_id}")
            logger.end(object={'api_limit_result': str(api_limit_result)})
            return api_limit_result
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
