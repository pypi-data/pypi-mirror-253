import os
import unittest
from unittest.mock import Mock, patch

from generalindex.GxApi import GxApi, _ApiRequest
from generalindex.exceptions import ApiResponseException

os.environ["NG_API_AUTHTOKEN"] = "test"


class ApiTestCase(unittest.TestCase):
    def test_given_dict_params_when_index_called_with_parsed_params(self):
        api = GxApi()
        param_dict = {'PeriodType': 'Month', 'TimeRef': '1200', 'Code': 'GX0123', 'From': '1v',
                      'metadata.test': 'value', 'metadata.test2': 'value2', 'Period': '1', 'testField': 'test'}

        response = api.index(["GX0123"], ["1"], ["Month"], time_ref=["1200"], start_from="1v",
                             metadata_fields={"metadata.test": "value", "metadata.test2": "value2"},
                             fields={'testField': "test"})
        self.assertTrue(response is not None)
        self.assertEqual(response.request_params(), param_dict)

    def test_given_dict_params_when_catalogue_called_with_parsed_params(self):
        api = GxApi()
        param_dict = {'Code': 'GX0123,GX01233', 'field.testField': 'test', 'NoModule': True, 'Module': 'TestModule'}

        catalogue = api.catalogue(["GX0123", "GX01233"], no_module=True, module='TestModule',
                                  fields={'field.testField': "test"}, limit_fields=["Code", "Test"])
        self.assertTrue(catalogue is not None)
        self.assertEqual(catalogue.request_params(), param_dict)
        self.assertEqual(catalogue.request_headers(), {"Fields": "Code,Test"})

    def test_given_query_params_when_csv_then_returns_stream(self):
        param_dict = {'PeriodType': 'Month', 'TimeRef': '1200', 'code': 'GX0123', 'from': '1v',
                      'metadata.test': 'value', 'period': '1', 'testField': 'test'}
        response_text = """Code,PeriodType,TimeRef,IndexModule,Alias,Bid,Commodity,Currency,DeliveryBasis,EndDate,
        FactsheetVersion,Frequency,Group,High,HolidayCalendar,Index,InterAffiliateDataAccepted,LastTradeDateCalendar,
        Low,MapLocation,Mid,Offer,ParentCodes,PeriodMax,PeriodMin,PermissionLatestStatus,Precision,PricingBasis,
        PriorityToTransactions,QaSeries,Quantity,SoleSourcedDataAccepted,Source,StartDate,Status,TimeRefDetails,
        TimeZone,Title,TradingHub,Units,Volume GX0006208,Prompt,1630,AmericasMarine,,,Marine Fuel,USD,Delivered,,2,
        Daily,Prod_Indexes,,Holidays_ICE_Brent,Y,N,,,20.6542084 -105.2458316,,,GX0002016,1,1,DEVELOPMENT,3,Flat,Y,,,
        N,GX,,New,Houston Close,America/Chicago,Intermediate Fuel Oil 180 CST Bunker Puerto Vallarta (MXPVR) Mexico,
        North America,MT,"""
        index = _ApiRequest('/index', param_dict)

        mock_caller = Mock()
        mock_caller.get.return_value.status_code = 200
        mock_caller.get.return_value.content = str.encode(response_text)

        with patch.object(index, "_caller", new=mock_caller):
            result = index.csv()
            calls = mock_caller.mock_calls
            self.assertTrue(result is not None)
            self.assertEqual(str(result.read(), encoding='utf-8'), response_text)
            self.assertDictEqual(
                calls[0].kwargs['query_params'], param_dict)
            self.assertDictEqual(
                calls[0].kwargs['headers'], {"Accept": "text/plain"})

    def test_given_status_401_when_csv_then_raises_exc(self):
        param_dict = {}
        response_text = """{
    "timestamp": "2023-12-19T10:03:43.246402281",
    "message": "User not authorized."}"""

        mock_caller = Mock()
        mock_caller.get.return_value.status_code = 503
        mock_caller.get.return_value.text = response_text
        index = _ApiRequest('/index', param_dict)
        with patch.object(index, "_caller", new=mock_caller):
            with self.assertRaises(ApiResponseException) as context:
                index.csv()

            self.assertTrue(
                'Response code 503.\n {\n    "timestamp": "2023-12-19T10:03:43.246402281",\n    "message": "User not '
                'authorized."}' in str(
                    context.exception))

    def test_given_query_params_when_json_then_returns_stream(self):
        param_dict = {'PeriodType': 'Month', 'TimeRef': '1200', 'code': 'GX0123', 'from': '1v',
                      'metadata.test': 'value', 'period': '1', 'testField': 'test'}

        response_text = """[
            {
                "Code": "GX0007205",
                "PeriodType": "Prompt",
                "TimeRef": "1630",
                "IndexModule": "EuropeanMarine",
                "Commodity": "Marine Fuel",
                "Currency": "USD",
                "DeliveryBasis": "Delivered",
                "FactsheetVersion": "2",
                "Frequency": "Daily",
                "Group": "Prod_Indexes",
                "HolidayCalendar": "Holidays_ICE_Brent",
                "Index": "Y",
                "InterAffiliateDataAccepted": "N",
                "MapLocation": "5.860754324 -10.05227963",
                "ParentCodes": "GX0000544",
                "PeriodMax": "1",
                "PeriodMin": "1",
                "PermissionLatestStatus": "DEVELOPMENT",
                "Precision": "3",
                "PricingBasis": "Flat",
                "PriorityToTransactions": "Y",
                "SoleSourcedDataAccepted": "N",
                "Source": "GX",
                "Status": "New",
                "TimeRefDetails": "London Close",
                "TimeZone": "Europe/London",
                "Title": "Marine Gasoil Bunker Buchanan (LRUCN) Liberia",
                "TradingHub": "West Africa",
                "Units": "MT"
            }
            ]"""
        index = _ApiRequest('/index', param_dict)
        mock_caller = Mock()
        mock_caller.get.return_value.status_code = 200
        mock_caller.get.return_value.content = str.encode(response_text)

        with patch.object(index, "_caller", new=mock_caller):
            result = index.json()
            calls = mock_caller.mock_calls
            self.assertTrue(result is not None)
            self.assertEqual(str(result.read(), encoding='utf-8'), response_text)
            self.assertDictEqual(
                calls[0].kwargs['query_params'], param_dict)
            self.assertDictEqual(
                calls[0].kwargs['headers'], {"Accept": "application/json"})

    def test_given_json_when_file_then_returns_stream(self):
        param_dict = {'PeriodType': 'Month', 'TimeRef': '1200', 'code': 'GX0123', 'from': '1v',
                      'metadata.test': 'value', 'period': '1', 'testField': 'test'}

        response_text = """[
            {
                "Code": "GX0007205",
               }
            ]"""
        index = _ApiRequest('/index', param_dict)
        mock_caller = Mock()
        mock_caller.get.return_value.status_code = 200
        mock_caller.get.return_value.content = str.encode(response_text)

        with patch.object(index, "_caller", new=mock_caller):
            index.file("/tmp/file", "json")
            calls = mock_caller.mock_calls

            self.assertDictEqual(
                calls[0].kwargs['query_params'], param_dict)
            self.assertDictEqual(
                calls[0].kwargs['headers'], {"Accept": "application/json"})

    def test_given_csv_params_when_file_then_returns_stream(self):
        param_dict = {'PeriodType': 'Month', 'TimeRef': '1200', 'code': 'GX0123', 'from': '1v',
                      'metadata.test': 'value', 'period': '1', 'testField': 'test'}
        response_text = "Code"
        index = _ApiRequest('/index', param_dict)
        mock_caller = Mock()
        mock_caller.get.return_value.status_code = 200
        mock_caller.get.return_value.content = str.encode(response_text)

        with patch.object(index, "_caller", new=mock_caller):
            index.file("/tmp/file", )
            calls = mock_caller.mock_calls
            self.assertDictEqual(
                calls[0].kwargs['query_params'], param_dict)
            self.assertDictEqual(
                calls[0].kwargs['headers'], {"Accept": "text/plain"})
