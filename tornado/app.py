from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import parse_command_line
from tornado import web, gen
import momoko
import os
import asyncio
import uvloop


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class BaseHandler(web.RequestHandler):
    @property
    def db(self):
        return self.application.db


class DB(BaseHandler):
    @gen.coroutine
    def get(self):
        cursor = yield self.db.execute("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
        self.write(cursor.fetchone()[0])
        self.finish()


def make_app():
    application = web.Application([
        (r'/db', DB)
    ], debug=True)
    ioloop = IOLoop.instance()

    application.db = momoko.Pool(
        dsn=os.environ['DATABASE_URL'],
        ioloop=ioloop,
    )

    future = application.db.connect()
    ioloop.add_future(future, lambda f: ioloop.stop())
    ioloop.start()
    future.result()  # raises exception on connection error

    http_server = HTTPServer(application)
    http_server.listen(8080, '0.0.0.0')
    ioloop.start()
    return application


app = make_app()
