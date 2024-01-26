from logger_local.LoggerLocal import Logger

from .api_management_local import APIManagementsLocal
from .constants import api_management_local_python_code

# TODO: Can we create a logger with api_type_id
logger = Logger.create_logger(object=api_management_local_python_code)


class APIMangementManager(APIManagementsLocal):
    def __init__(self) -> None:
        super().__init__()

    def seconds_to_sleep_after_passing_the_hard_limit(self, api_type_id: int):
        # TODO Can we update the logger internal object and add api_type_id to all logger records?
        try:
            hard_limit_value, hard_limit_unit = self.get_hard_limit_by_api_type_id(api_type_id=api_type_id)
            # we must use the subquery_alias because the subquery must have an alias
            query = f"""SELECT TIMESTAMPDIFF(SECOND, NOW(), 
                        (SELECT TIMESTAMPADD({hard_limit_unit}, 1, MIN(start_timestamp)) 
                        FROM (SELECT start_timestamp 
                                FROM api_call.api_call_view
                                WHERE api_type_id = %s AND is_network=TRUE 
                                ORDER BY api_call_id DESC LIMIT %s) AS subquery_alias
                                )
                        )"""

            self.cursor.execute(query, (api_type_id, hard_limit_value))
            seconds_to_sleep_after_passing_the_hard_limit = self.cursor.fetchone()[0]

            logger.end("seconds_to_sleep_after_passing_the_hard_limit = " + str(
                seconds_to_sleep_after_passing_the_hard_limit))
            return seconds_to_sleep_after_passing_the_hard_limit

        except Exception as exception:
            logger.exception("exception=" + str(exception), object=exception)
            logger.end()
            raise  # Raise the exception for higher-level handling
