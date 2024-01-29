from requests.structures import CaseInsensitiveDict
from yeedu.utility.json_utils import response_validator
from yeedu.utility.request_utils import Requests
from yeedu.utility.logger_utils import Logger
from yeedu import config
import requests
import sys

logger = Logger.get_logger(__name__, True)


class DownloadClusterInstanceLogs:
    def get_cluster_instance_log_records(log_type, cluster_id=None, cluster_name=None):
        try:
            url = f"{config.YEEDU_RESTAPI_URL}/cluster/log/{log_type}"

            response = Requests(
                url=url,
                method="GET",
                headers=config.headers,
                stream=True,
                params={
                    "cluster_id": cluster_id,
                    "cluster_name": cluster_name
                }
            ).send_http_request()

            if (response.status_code == 200 and CaseInsensitiveDict(response.headers).get('Content-Type') == 'text/plain' and CaseInsensitiveDict(response.headers).get('Content-disposition')):
                try:
                    for line in response.iter_lines(decode_unicode=True):
                        if line:
                            logger.info(line)

                    return True, response.status_code

                except Exception as e:
                    logger.exception(
                        f"Failed to get cluster instance logs due to : {e}")
                    sys.exit(-1)
            else:
                return response_validator(response)

        except requests.exceptions.RequestException as e:
            logger.exception(f"Failed to connect due to {e}")
            sys.exit(-1)
