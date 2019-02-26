from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado import web
from functools import partial
import os
import asyncio
import uvloop
import asyncpg


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class BaseHandler(web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class DBHandler(BaseHandler):
    async def get(self):
        async with self.db.acquire() as connection:
            result = await connection.fetchval("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
        self.write(result)


async def init_db():
    return await asyncpg.create_pool(dsn=os.environ['DATABASE_URL'])


def make_app():
    application = web.Application([
        (r'/db', DBHandler)
    ])

    uvloop.install()

    server = HTTPServer(application)
    server.listen(8080, '0.0.0.0')

    ioloop = IOLoop.current()
    application.db = ioloop.run_sync(partial(init_db))

    ioloop.start()

    return application


app = make_app()
