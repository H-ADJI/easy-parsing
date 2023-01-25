
from parsel import Selector


class EasyParser():
    def __init__(self, html: str) -> None:
        self._selector = Selector(html)
        self.data_mapping = {}

    def get(self, alias: str, xpath: str):
        def decorator(func):
            selected = self._selector.xpath(query=xpath)
            element = selected.get()

            self.data_mapping[alias] = func(element)
        return decorator

    def get_all(self, alias: str, xpath: str):
        def decorator(func):
            selected = self._selector.xpath(query=xpath)
            element = selected.getall()
            self.data_mapping[alias] = func(element)
        return decorator
