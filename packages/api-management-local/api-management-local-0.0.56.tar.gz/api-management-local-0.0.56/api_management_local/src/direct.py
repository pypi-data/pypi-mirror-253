import http
import json

import requests
from logger_local.LoggerLocal import Logger
from star_local.star_local import StarsLocal

from .Exception_API import PassedTheHardLimitException
from .api_call import APICallsLocal
from .api_limit_status import APILimitStatus
from .api_management_local import APIManagementsLocal
from .api_type import ApiTypesLocal
from .constants import api_management_local_python_code
from .external_user_id import get_extenal_user_id_by_api_type_id

logger = Logger.create_logger(object=api_management_local_python_code)


class Direct:
    def __init__(self) -> None:
        self.api_type_local = ApiTypesLocal()
        self.api_call_local = APICallsLocal()
        self.api_management_local = APIManagementsLocal()

    def try_to_call_api(self, external_user_id: int, api_type_id: int, endpoint: str, outgoing_body: dict,
                        outgoing_header: dict) -> dict:
        logger.start(object={
            'external_user_id': str(external_user_id), 'api_type_id': str(api_type_id),
            'endpoint': str(endpoint), 'outgoing_body': str(outgoing_body), 'outgoing_header': str(outgoing_header)})
        action_id = self.api_type_local.get_action_id_by_api_type_id(api_type_id)
        StarsLocal.profile_star_before_action(action_id)
        self.api_management_local.sleep_per_interval(api_type_id)

        external_user_id = external_user_id or get_extenal_user_id_by_api_type_id(api_type_id)

        try:
            arr, outgoing_body_significant_fields_hash = self.api_management_local.check_cache(
                api_type_id, outgoing_body)
            if arr is None:
                check = self.api_management_local.check_limit(
                    external_user_id=external_user_id, api_type_id=api_type_id)
                logger.info("check= " + str(check))
                if check == APILimitStatus.BETWEEN_SOFT_LIMIT_AND_HARD_LIMIT:
                    logger.warn("You excced the soft limit")
                if check != APILimitStatus.GREATER_THAN_HARD_LIMIT:
                    output = requests.post(url=endpoint, data=outgoing_body, headers=outgoing_header)
                    status_code = output.status_code
                    text = output.text
                    incoming_message = output.content.decode('utf-8')
                    response_body = output.json()
                    response_body_str = json.dumps(response_body)
                    if http.HTTPStatus.OK == status_code:
                        StarsLocal.api_executed(api_type_id=api_type_id)
                    is_network = 1
                    api_call_json = {
                        'api_type_id': api_type_id, 'external_user_id': external_user_id,
                        'endpoint': endpoint, 'outgoing_header': str(outgoing_header),
                        'outgoing_body': str(outgoing_body),
                        'outgoing_body_significant_fields_hash': outgoing_body_significant_fields_hash,
                        'incoming_message': incoming_message, 'http_status_code': status_code,
                        'response_body': response_body_str,
                        'is_network': is_network
                    }
                    api_call_id = self.api_call_local.insert_api_call_json(api_call_json)
                    logger.end("check= " + str(check),
                               object={'status_code': status_code, 'text': text, 'api_call_id': api_call_id})
                    # return request("post", url=endpoint, data=outgoing_body, json=json, **kwargs)
                    return {'status_code': status_code, 'text': text, 'api_call_id': api_call_id}

                else:
                    logger.error("you passed the hard limit")
                    raise PassedTheHardLimitException
            else:
                status_code = arr[0]
                text = arr[1]
                is_network = 0
                incoming_message = ""
                response_body = ""
                api_call_json = {'api_type_id': api_type_id, 'external_user_id': external_user_id,
                                 'endpoint': endpoint, 'outgoing_header': str(outgoing_header),
                                 'outgoing_body': str(outgoing_body),
                                 'outgoing_body_significant_fields_hash': outgoing_body_significant_fields_hash,
                                 'incoming_message': incoming_message, 'http_status_code': status_code,
                                 'response_body': response_body,
                                 'is_network': is_network
                                 }
                StarsLocal.api_executed(api_type_id=api_type_id)
                api_call_id = self.api_call_local.insert_api_call_json(api_call_json)
                logger.info("bringing result from cache in database", object={
                    'status_code': status_code, 'text': text, 'api_call_id': api_call_id})
                return {'status_code': status_code, 'text': text, 'api_call_id': api_call_id}
        except Exception as exception:
            logger.exception("exception=" + str(exception), object=exception)
            logger.end()
            raise exception
