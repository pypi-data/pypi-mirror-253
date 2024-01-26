import http
import json
import random
import sys
import time

import requests
from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerLocal import Logger

from .Exception_API import ApiTypeDisabledException, ApiTypeIsNotExistException
from .api_limit import APILimitsLocal
from .api_limit_status import APILimitStatus
from .constants import api_management_local_python_code

logger = Logger.create_logger(object=api_management_local_python_code)


class APIManagementsLocal(GenericCRUD):
    def __init__(self) -> None:
        super().__init__(default_schema_name="api_type", default_id_column_name="api_type_id",
                         default_table_name="api_type_table", default_view_table_name="api_type_view")
        self.api_limits = APILimitsLocal()

    def delete_api(self, external_user_id: int, api_type_id: int, endpoint: str, data: dict) -> requests.Response:
        """Returns the response of the delete request"""
        logger.start(object={'external_user_id': str(external_user_id), 'api_type_id': str(api_type_id), 'data': data})
        response = None
        try:
            check_limit = self.check_limit(external_user_id=external_user_id, api_type_id=api_type_id)

            if check_limit == APILimitStatus.BELOW_SOFT_LIMIT:
                response = requests.delete(endpoint, data=data)

            elif check_limit == APILimitStatus.BETWEEN_SOFT_LIMIT_AND_HARD_LIMIT:
                logger.warn("you passed the soft limit")

            else:
                logger.error("you passed the hard limit")
                # TODO Shall we raise our user defined extension?

        except Exception as exception:
            logger.exception("exception=" + str(exception), object=exception)
            raise
        finally:  # This is done in any case
            logger.end("response=" + str(response))
            return response

    def get_api(self, external_user_id: int, api_type_id: int, endpoint: str, data: dict) -> requests.Response:
        """Returns the response of the get request"""
        logger.start(object={'external_user_id': str(external_user_id), 'api_type_id': str(api_type_id), 'data': data})
        response = None
        try:
            check_limit = self.check_limit(external_user_id=external_user_id, api_type_id=api_type_id)

            if check_limit == APILimitStatus.BELOW_SOFT_LIMIT:
                response = requests.get(endpoint, data=data)

            elif check_limit == APILimitStatus.BETWEEN_SOFT_LIMIT_AND_HARD_LIMIT:
                logger.warn("you passed the soft limit")

            else:
                logger.error("you passed the hard limit")
                # TODO Shall we raise our user defined exception

        except Exception as exception:
            logger.exception("exception=" + str(exception), object=exception)
            raise
        finally:
            logger.end("response=" + str(response))
            return response

    def put_api(self, external_user_id: int, api_type_id: int, endpoint: str, data: dict) -> requests.Response:
        """Returns the response of the put request"""
        logger.start(object={'external_user_id': str(external_user_id), 'api_type_id': str(api_type_id), 'data': data})
        response = None
        try:
            check_limit = self.check_limit(external_user_id=external_user_id, api_type_id=api_type_id)

            if check_limit == APILimitStatus.BELOW_SOFT_LIMIT:
                response = requests.put(endpoint, data=data)

            elif check_limit == APILimitStatus.BETWEEN_SOFT_LIMIT_AND_HARD_LIMIT:
                logger.warn("you passed the soft limit")

            else:
                logger.error("you passed the hard limit")

        except Exception as exception:

            logger.exception("exception=" + str(exception), object=exception)
            raise
        finally:
            logger.end("response=" + str(response))
            return response

    def _second_from_last_network_api(self, api_type_id: int) -> int:
        """Returns the number of seconds from the last network api call of the given api_type_id"""
        logger.start(object={'api_type_id': str(api_type_id)})
        query = f"""SELECT TIMESTAMPDIFF(SECOND, start_timestamp, NOW()) 
                    FROM api_call.api_call_view 
                    WHERE api_type_id=%s AND is_network=TRUE 
                    ORDER BY start_timestamp DESC
                    LIMIT 1"""
        self.cursor.execute(query, (api_type_id,))
        results = self.cursor.fetchone()
        if not results:
            logger.end(object={'second_from_last_network_api': 0})
            second_from_last_network_api = sys.maxsize
        else:
            second_from_last_network_api = results[0]
        logger.info("second_from_last_network_api = " + str(second_from_last_network_api))
        return second_from_last_network_api

    def get_hard_limit_by_api_type_id(self, api_type_id: int) -> (int, str):
        """Returns the hard limit value and unit of the given api_type_id"""
        logger.start(object={'api_type_id': str(api_type_id)})
        try:
            self.set_schema("api_limit")
            result = self.select_one_tuple_by_id(view_table_name="api_limit_view",
                                                 id_column_name="api_type_id", id_column_value=api_type_id,
                                                 select_clause_value="hard_limit_value,hard_limit_unit")
            logger.end(object={'hard_limit_value': result[0], 'hard_limit_unit': result[1]})
            return result

        except Exception as exception:
            logger.exception("exception=" + str(exception), object=exception)
            raise exception

    def get_actual_api_succ_network_by_api_type_id_last_x_units(
            self, external_user_id: int, api_type_id: int, value: int, unit: str) -> int:
        """Returns the number of successful network api calls of the given api_type_id in the last x units"""
        logger.start(object={'api_type_id': str(api_type_id), 'value': str(value), 'unit': unit})

        try:
            query = f"""
                SELECT COUNT(*) FROM api_call.api_call_view
                WHERE api_type_id = %s AND external_user_id = %s
                    AND TIMESTAMPDIFF({unit}, created_timestamp, NOW()) <= %s
                    AND http_status_code = %s AND is_network=TRUE
            """
            self.cursor.execute(query, (api_type_id, external_user_id, value, http.HTTPStatus.OK.value))
            actual_succ_count = self.cursor.fetchone()
            if not actual_succ_count:
                raise Exception(f"no succ count found for api_type_id={api_type_id}, "
                                f"external_user_id={external_user_id}, value={value}, unit={unit}")
            logger.end(object={'actual_succ_count': actual_succ_count[0]})
            return actual_succ_count[0]

        except Exception as exception:
            logger.exception(object=exception)
            logger.end()

    def sleep_per_interval(self, api_type_id: int) -> None:
        """Sleeps for a random interval between the min and max interval of the given api_type_id"""
        logger.start(object={'api_type_id': str(api_type_id)})
        self.set_schema("api_type")
        interval_min_seconds, interval_max_seconds = self.select_one_tuple_by_where(
            view_table_name="api_type_view", where="is_enabled=TRUE AND api_type_id=%s",
            params=(api_type_id,), select_clause_value="interval_min_seconds, interval_max_seconds")
        self._verify_api_type_exists_and_enabled(api_type_id)
        random_interval = random.uniform(
            interval_min_seconds, interval_max_seconds)
        logger.info("interval_min_seconds= " + str(interval_min_seconds) + " interval_max_seconds= " +
                    str(interval_max_seconds) + " random_interval= " + str(random_interval))
        second_from_last_network_api = self._second_from_last_network_api(api_type_id)
        if random_interval > second_from_last_network_api:
            sleep_second = random_interval - second_from_last_network_api
            logger.info("sleeping " + str(sleep_second) + " seconds")
            time.sleep(sleep_second)
        else:
            logger.info("No sleep needed")
            logger.end()

    def check_cache(self, api_type_id: int, outgoing_body: dict) -> (int, str, int):
        """Returns the http_status_code, response_body and outgoing_body_significant_fields_hash
            of the cached api call of the given api_type_id and outgoing_body"""
        logger.start(object={'api_type_id': str(api_type_id), 'outgoing_body': outgoing_body})

        try:
            outgoing_body_significant_fields_hash = hash(
                self._get_json_with_only_sagnificant_fields_by_api_type_id(
                    data_json=outgoing_body, api_type_id=api_type_id))
            query = f"""SELECT http_status_code, response_body 
                            FROM api_call.api_call_view JOIN api_type.api_type_view 
                                ON api_type.api_type_view.api_type_id = api_call.api_call_view.api_type_id
                            WHERE api_call_view.api_type_id= %s AND http_status_code=200
                                AND TIMESTAMPDIFF(MINUTE , api_call.api_call_view.start_timestamp, NOW())
                                        <= api_type_view.expiration_value
                                AND outgoing_body_significant_fields_hash=%s 
                                AND is_network=TRUE
                            ORDER BY api_call_id DESC LIMIT 1"""
            self.cursor.execute(query, (api_type_id, outgoing_body_significant_fields_hash))
            logger.end()
            return self.cursor.fetchone(), outgoing_body_significant_fields_hash
        except Exception as exception:
            logger.exception("exception=" + str(exception), object=exception)
            logger.end()
            raise exception

    def check_limit(self, external_user_id: int, api_type_id: int) -> APILimitStatus:
        """Returns the APILimitStatus of the given external_user_id and api_type_id"""
        logger.start(object={'external_user_id': external_user_id, 'api_type_id': str(api_type_id)})
        api_limits_tuple = self.api_limits.get_api_limit_tuple_by_api_type_id_external_user_id(
            api_type_id, external_user_id)
        soft_limit_value = api_limits_tuple[0]
        soft_limit_unit = api_limits_tuple[1]
        hard_limit_value = api_limits_tuple[2]
        # hard_limit_unit=limits[3]
        api_succ = self.get_actual_api_succ_network_by_api_type_id_last_x_units(
            external_user_id, api_type_id, soft_limit_value, soft_limit_unit)

        # TODO if not GREATER_THAN_HARD_LIMIT check_money_budget()

        if api_succ < soft_limit_value:
            return APILimitStatus.BELOW_SOFT_LIMIT
        elif soft_limit_value <= api_succ < hard_limit_value:
            return APILimitStatus.BETWEEN_SOFT_LIMIT_AND_HARD_LIMIT
        else:
            return APILimitStatus.GREATER_THAN_HARD_LIMIT

    def _get_json_with_only_sagnificant_fields_by_api_type_id(self, data_json: dict, api_type_id: int) -> json:
        """Returns the json with only the significant fields of the given data_json and api_type_id"""
        logger.start(object={'data_json': data_json, 'api_type_id': api_type_id})
        try:
            self.set_schema("api_type")
            result = self.select_multi_dict_by_where(view_table_name="api_type_field_view",
                                                     where="api_type_id=%s AND field_significant = TRUE",
                                                     params=(api_type_id,), select_clause_value="field_name")

            # TODO Support hierarchy fields in json like we have in messages i.e. Body.Text.Data,
            #  please also add tests based on data we have in our api_call_table
            significant_fields = [row["field_name"] for row in result]
            filtered_data = {key: data_json[key]
                             for key in significant_fields if key in data_json}
            filtered_json = json.dumps(filtered_data)
            logger.end(object={'filtered_json': str(filtered_json)})
            return filtered_json
        except Exception as exception:
            logger.exception("exception" + str(exception), object=exception)
            logger.end()

    def _verify_api_type_exists_and_enabled(self, api_type_id: int) -> None:
        """Checks if the given api_type_id exists and enabled
            and raises ApiTypeIsNotExistException or ApiTypeDisabledException if not"""
        is_enabled = self.select_one_dict_by_id(view_table_name="api_type_view", id_column_value=api_type_id,
                                                select_clause_value="is_enabled")
        if not is_enabled:
            raise ApiTypeIsNotExistException
        elif is_enabled["is_enabled"] == 0:
            raise ApiTypeDisabledException

    # TODO Develop incoming_api
    # def incoming_api(self, api_call_json: str):
    #     api_call.insert( api_call_json )
