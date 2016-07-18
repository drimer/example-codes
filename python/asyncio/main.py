'''This example shows one way of using asyncio to parallelise the work of
various coroutines.

By using the loop's "run_until_complete()" method, we kick off the loop to do
its job. If we wanted an infinite set of coroutines running, we would just
change "say_hello()" so that it yields from those other coroutines inside an
infinite loop.
'''


import random

import asyncio


async def say_hello(name):
    secs = random.choice(range(9))
    await asyncio.sleep(secs)  #  time.sleep() would block the whole main loop
    print('hi {}'.format(name))


loop = asyncio.get_event_loop()
all_names = ('Bob', 'John', 'Mike', 'Danny', 'Smith', 'Clark')
futures = [say_hello(name) for name in all_names]
loop.run_until_complete(asyncio.gather(*futures))