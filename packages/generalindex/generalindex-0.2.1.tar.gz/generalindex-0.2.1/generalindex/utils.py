from urllib import parse

from .exceptions import MissingArgumentException
from .constants import LOGGER_NAME
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.Logger(LOGGER_NAME)

logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log.addHandler(logger_handler)

def is_blank(param):
    return param in ["", None]


class PathFormatter:
    def get_symbol_queried_path(self, _size=1000, start=0, group_name=None, search_for=None):
        formatted_query = self._get_symbol_queries(group_name, search_for)
        return '/ts/symbol/search?size={}&from={}&query={}'.format(_size, start,
                                                                   formatted_query)

    def _get_symbol_queries(self, group_name, search_for):

        if (is_blank(group_name)) and (is_blank(search_for)):
            raise MissingArgumentException(
                'Please specify either group_name or search_for parameter of get_symbols() method')

        formatted_group = self._parse_symbol_query(group_name)
        formatted_search = self._parse_symbol_query(search_for)

        if not is_blank(formatted_search) and not is_blank(formatted_group):
            return '{}*%26groupName.keyword%3D{}'.format(
                formatted_search,
                formatted_group)
        elif not is_blank(formatted_search):
            return formatted_search
        else:
            return 'groupName.keyword%3D{}'.format(
                formatted_group)

    @staticmethod
    def _parse_symbol_query(symbol_query):
        if not is_blank(symbol_query):
            return parse.quote(symbol_query)
        else:
            return None
