import asyncio

import aiohttp

url = "http://127.0.0.1:2001?q={}"


@asyncio.coroutine
def request_greeting(url):
    resp = yield from aiohttp.get(url)
    text = yield from resp.text()
    return text


loop = asyncio.get_event_loop()

ingredients = ('eggs', 'milk', 'spam')
futures = [request_greeting(url.format(ing)) for ing in ingredients]

greetings = loop.run_until_complete(asyncio.gather(*futures))
print('\n'.join(greetings))

loop.close()
