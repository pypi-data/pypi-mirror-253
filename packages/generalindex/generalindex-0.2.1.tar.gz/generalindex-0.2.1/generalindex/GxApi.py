import inspect
import json
from io import BytesIO
from typing import Literal

from .HTTPCaller import HTTPCaller
from .exceptions import ApiResponseException
from .utils import PathFormatter

MetadataVals = Literal["true", "false", "only"]
OrderVals = Literal["asc", "desc"]
OutputTypes = Literal["csv", "json"]


class GxApi:
    @staticmethod
    def get_symbols(search: str = None, group_name: str = 'Prod_Indexes', size=1000, start_from=0):
        '''
        Returns a list of the symbols available on a given group or symbols within search
        '''
        query_url = PathFormatter().get_symbol_queried_path(start=start_from, _size=size, group_name=group_name,
                                                            search_for=search)
        return json.load(_ApiRequest(path=query_url).json())

    def index(self, code: list = None, period: list = None, period_type: list = None,
              time_ref: list = None, group: str = None, module: list = None,
              start_from: str = None,
              to: str = None, delta: bool = None,
              metadata: MetadataVals = None,
              metadata_fields: dict = None, order: OrderVals = None, timezone: str = None,
              fields: dict = None):
        """
        The method retrieves the data from Gx Api based on provided parameters.

        :param code: Symbol code (default '*' )
        :param period: Symbol period (default '*' ).
        :param period_type: Symbol periodType (default '*' )
        :param time_ref: Symbol timeRef (default '*' )
        :param group: Name of the group (default Prod_Indexes)
        :param module: Name of the IndexModule. Can't use with 'code','period','periodType' and 'timeRef' parameter
        :param start_from: Start date (default beginning of the day) Accepted values:
            today
            *d - specific amount of days
            *m - specific amount of months
            *y - specific amount of years
            all- no specified starting point
            {x}v- only x last values for each index
            ISO date ex. 2022-11-21T00:00:00
            where * is a number
        :param to: End date (default end of the day) Accepted values:
            today
            *d - specific amount of days
            *m - specific amount of months
            *y - specific amount of years
            ISO date ex. 2022-11-21T00:00:00
            where * is a number

        :param delta: Delta will filter timeseries by insertion date instead of the actual timestamp of data (default false)
        :param metadata: Metadata (default false) Accepted values: true, false, only
        :param metadata_fields: Filter by metadata field e.g. {"metadata.tradinghub":"NWE"}
        :param order: Order of results by date (default desc)
        :param timezone: Timezone as string used for the timestamps in the Date column.
        Continent/City, for example Europe/London (default UTC)
        :param fields: Filter by value field e.g. {"FactsheetVersion":"1"}

        :return: _ApiRequest
        """
        sig, method_locals = inspect.signature(self.index), locals()
        query_params_dict = {self._to_camel_case(param.name): self._concatenate(method_locals[param.name]) for param in
                             sig.parameters.values() if
                             (method_locals[param.name] is not None)}
        query_params_dict = self._create_query_params(query_params_dict)
        return _ApiRequest(path='/index', query_params=query_params_dict)

    def catalogue(self, code: list = None, no_module: bool = None, module: str = None,
                  fields: dict = None, limit_fields: list = None):
        """
        The method retrieves the data from Gx Api based on provided parameters.

        :param code: Symbol code (default '*' )
        :param no_module: Include indexes without index module set (default false)
        :param module: Filter by provided IndexModule name
        :param fields: Filter by catalogue field e.g. {"field.status":"Live"}
        :param limit_fields: Limit request to specified fields e.x. 'Code,Title'

        :return: _ApiRequest
        """
        sig, method_locals = inspect.signature(self.catalogue), locals()
        query_params_dict = {self._to_camel_case(param.name): self._concatenate(method_locals[param.name]) for param in
                             sig.parameters.values() if
                             (method_locals[param.name] is not None) & (param.name != 'limit_fields')}
        query_params_dict = self._create_query_params(query_params_dict)
        limit_header = {}
        if limit_fields is not None:
            limit_header = {"Fields": self._concatenate(limit_fields)}
        return _ApiRequest(path='/catalogue', query_params=query_params_dict, headers=limit_header)

    def _create_query_params(self, query_params_dict):
        self._flat_map(query_params_dict, "MetadataFields")
        self._flat_map(query_params_dict, "Fields")

        return query_params_dict

    @staticmethod
    def _concatenate(params):
        if type(params) is not list:
            return params
        else:
            query = params.pop(0)
            for s in params:
                query += ','
                query += s

            return query

    @staticmethod
    def _flat_map(query_params_dict, key):
        _dict = query_params_dict.pop(key, None)
        if _dict:
            query_params_dict.update(_dict)

    @staticmethod
    def _to_camel_case(name):
        if name == 'start_from':
            name = 'from'
        return "".join(x.capitalize() for x in name.lower().split("_"))


class _ApiRequest:
    def __init__(self, path, query_params=None, headers: dict = None):
        self._caller = HTTPCaller()
        self._headers = headers
        self._path = path
        self._query_params = query_params

    def csv(self):
        self._update_headers({"Accept": 'text/plain'})
        response = self._caller.get(self._path, headers=self._headers, query_params=self._query_params)
        return self.verify_response(response)

    def json(self):
        self._update_headers({"Accept": 'application/json'})
        response = self._caller.get(self._path, headers=self._headers, query_params=self._query_params)
        return self.verify_response(response)

    def file(self, file_name, output_type: OutputTypes = "csv"):
        if output_type == "csv":
            self._update_headers({"Accept": 'text/plain'})
        else:
            self._update_headers({"Accept": 'application/json'})

        response = self._caller.get(self._path, headers=self._headers, query_params=self._query_params)
        file_name = file_name if '.' in file_name else file_name + '.' + output_type
        with open(file_name, "wb") as text_file:
            text_file.write(self.verify_response(response).read())

    @staticmethod
    def verify_response(response):
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            raise ApiResponseException("Response code {}.\n {}".format(response.status_code, response.text))

    def request_params(self):
        return self._query_params

    def request_headers(self):
        return self._headers

    def _update_headers(self, param):
        if self._headers is None:
            self._headers = {}
        self._headers.update(param)
