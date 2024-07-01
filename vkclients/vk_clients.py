from .reader import Reader
from vkbottle import API, VKAPIError
from vkbottle.user import User
from random import choice
import re


class VkClients(Reader):
    def __init__(self, proxies_file, tokens_file):
        super().__init__(proxies_file, tokens_file)
        self.clients: list[User] = []
        self.get_clients()

    def get_clients(self):
        for token in self.tokens:
            api = API(token=token, http_client=self.proxy)
            user = User(api=api)
            self.clients.append(user)

    async def get_post(self, domain):
        client = choice(self.clients)
        reg = re.findall(r'(?:(?<=club)|(?<=id)|(?<=public))\d+$', domain)
        owner_id = None
        if len(reg) == 1:
            owner_id = int(reg[0])
            if not 'id' in domain:
                owner_id = -owner_id
        post = await client.api.wall.get(domain=domain, owner_id=owner_id, count=1)
        return post.items[0].owner_id, post.items[0].id

    async def add_likes(self, domain):
        count = 0
        try:
            owner_id, post_id = await self.get_post(domain)
        except VKAPIError:
            return count, None
        for client in self.clients:
            try:
                await client.api.likes.add('post', item_id=post_id, owner_id=owner_id)
            except VKAPIError:
                continue
            count += 1
        url = f'https://vk.com/wall{owner_id}_{post_id}'
        return count, url
