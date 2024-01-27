import requests
import requests.packages
import logging
from json import JSONDecodeError
from datetime import date
from typing import Dict, Type
from .models import Result, Employee, Position, Category, Shift, TimeOff
from .exceptions.w2w_bad_request import W2WBadRequestException
from .exceptions.w2w_bad_type import W2WBadType

endpoint_return_classes: dict[str, Type[Position | Employee | Category | TimeOff]] = {
    'EmployeeList': Employee,
    'PositionList': Position,
    'CategoryList': Category,
    'AssignedShiftList': Shift,
    'ApprovedTimeOff': TimeOff
}


class Adapter:
    def __init__(self, hostname: str, api_key: str, ssl_verify: bool = True, logger: logging.Logger = None):
        """
        Constructor for Client

        :param hostname: WhenToWork Host
        :param api_key: API key provided by W2W, used for authentication
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: If your app has a logger, pass it in here.
        """

        self.url = f"https://{hostname}/api/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        if not ssl_verify:
            # noinspection PyUnresolvedReferences
            requests.packages.urllib3.disable_warnings()
        self._logger = logger or logging.getLogger(__name__)

    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None) -> Result:
        full_url = self.url + endpoint
        if ep_params:
            ep_params.update({'key': self._api_key})
        else:
            ep_params = {'key': self._api_key}
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify,
                                        params=ep_params)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise W2WBadRequestException("Request failed") from e
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError, requests.exceptions.JSONDecodeError) as e:
            # self._logger.error(msg=log_line_post.format(False, None, e))
            raise W2WBadRequestException("Bad JSON in response") from e
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        log_line = f"{is_success}, {response.status_code}, {response.reason})"
        if is_success:  # OK
            self._logger.debug(msg=log_line)
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise W2WBadRequestException(f"{response.status_code}: {response.reason}")

    def _get(self, endpoint: str, ep_params: Dict = None) -> Result:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)

    def get_from_endpoint(self, endpoint: str, start_date: date = None, end_date: date = None):
        if start_date and not isinstance(start_date, date):
            raise W2WBadType(f"start_date ({start_date}) not valid date type")
        if end_date and not isinstance(end_date, date):
            raise W2WBadType(f"end_date ({end_date}) not valid date type")
        if start_date and end_date:
            ep_params = {'start_date': start_date.strftime('%m/%d/%Y'), 'end_date': end_date.strftime('%m/%d/%Y')}
        else:
            ep_params = None
        stripped_data = self._get(endpoint=endpoint, ep_params=ep_params).data[endpoint]
        return [endpoint_return_classes[endpoint](data=item) for item in stripped_data]
