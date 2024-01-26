import http

from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerLocal import Logger
from star_local.star_local import StarsLocal

from .api_call import APICallsLocal
from .api_management_local import APIManagementsLocal
from .api_type import ApiTypesLocal
from .constants import api_management_local_python_code
from .external_user_id import get_extenal_user_id_by_api_type_id

logger = Logger.create_logger(object=api_management_local_python_code)


class InDirect(GenericCRUD):
    def __init__(self) -> None:
        super().__init__(default_schema_name="api_call", default_table_name="api_call_table",
                         default_view_table_name="api_call_view", default_id_column_name="api_call_id")
        self.api_type_local = ApiTypesLocal()
        self.api_call_local = APICallsLocal()
        self.api_management_local = APIManagementsLocal()

    def before_call_api(self, external_user_id: int, api_type_id: int, endpoint: str, outgoing_body: dict,
                        outgoing_header: dict):
        action_id = self.api_type_local.get_action_id_by_api_type_id(api_type_id)
        StarsLocal.profile_star_before_action(action_id)
        self.api_management_local.sleep_per_interval(api_type_id)
        if external_user_id is None:
            external_user_id = get_extenal_user_id_by_api_type_id(api_type_id)
        arr, outgoing_body_significant_fields_hash = self.api_management_local.check_cache(
            api_type_id, outgoing_body)
        if arr is None:
            is_network = None
            limit = self.api_management_local.check_limit(
                external_user_id=external_user_id, api_type_id=api_type_id)

        else:
            limit = None
            is_network = 0

        api_call_json = {'api_type_id': api_type_id, 'external_user_id': external_user_id,
                         'endpoint': endpoint, 'outgoing_header': str(outgoing_header),
                         'outgoing_body': str(outgoing_body),
                         'outgoing_body_significant_fields_hash': outgoing_body_significant_fields_hash,
                         'is_network': is_network
                         }
        api_call_id = self.api_call_local.insert_api_call_json(api_call_json=api_call_json)

        return limit, api_call_id, arr

    def after_call_api(self, external_user_id: int, api_type_id: int, endpoint: str, outgoing_body: dict,
                       outgoing_header: dict, http_status_code: int, response_body: str, incoming_message: str,
                       api_call_id: int, used_cache: bool):
        if http.HTTPStatus.OK == http_status_code:
            StarsLocal.api_executed(api_type_id=api_type_id)

        if used_cache:
            is_network = 0
        else:
            is_network = 1
        if external_user_id is None:
            external_user_id = get_extenal_user_id_by_api_type_id(api_type_id)
        # where="api_call_id= {}".format(api_call_id)
        update_data = {'external_user_id': external_user_id, 'endpoint': endpoint, 'outgoing_body': str(outgoing_body),
                       'outgoing_header': str(outgoing_header), 'http_status_code': http_status_code,
                       'response_body': str(response_body), 'incoming_message': str(incoming_message),
                       'is_network': is_network}
        super().update_by_id(id_column_value=api_call_id, data_json=update_data)
