from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine
import time

URLS = ['http://127.0.0.1:2001?q=milk',
       'http://127.0.0.1:2001?q=eggs',
       'http://127.0.0.1:2001?q=spam']

@coroutine
def get_greetings():
    http_client = AsyncHTTPClient()
    responses = yield [http_client.fetch(url) for url in URLS]
    return '\n'.join([resp.body.decode('utf8') for resp in responses])


if __name__ == "__main__":
    loop = IOLoop.instance()
    t1 = time.time()
    text = loop.run_sync(get_greetings)
    print(time.time() - t1, "seconds passed")
    print(text)