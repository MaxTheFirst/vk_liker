from vkbottle.http import AiohttpClient
from aiohttp import ClientSession
from aiohttp_proxy import ProxyConnector


class Reader():
    def __init__(self, proxies_file, tokens_file):
        self.proxies = self.read_file(proxies_file)
        self.tokens = self.read_file(tokens_file)

    def read_file(self, file_name):
        with open(file_name) as file:
            data = file.readlines()
        return [i.strip() for i in data if i != '']

    def get_item(self, items: list) -> str:
        if items:
            return items.pop(0)

    @property
    def proxy(self):
        proxy = self.get_item(self.proxies)
        if proxy:
            url, login_passwoard = proxy.split('#')
            proxy = f'http://{login_passwoard}@{url}'
            connector = ProxyConnector.from_url(proxy)
            session = ClientSession(connector=connector)
            return AiohttpClient(session=session)
