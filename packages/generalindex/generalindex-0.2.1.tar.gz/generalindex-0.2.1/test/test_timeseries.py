import os
import unittest
from generalindex import Timeseries

os.environ["NG_API_AUTHTOKEN"] = "test"


class TimeseriesTestCase(unittest.TestCase):
    def test_given_wrong_timezone_when_verify_then_raise_exc(self):
        with self.assertRaises(ValueError) as context:
            Timeseries.verify_timezone("UFX")

        self.assertTrue(
            'Wrongly formatted timezone argument. Must be for example Europe/London' in str(context.exception))

    def test_given_correct_timezone_when_verify_returns_true(self):
        params = [
            "UTC",
            "Europe/London",
            "US/Hawaii",
        ]
        for i in params:
            with self.subTest(i=i):
                self.assertTrue(Timeseries.verify_timezone(i))
