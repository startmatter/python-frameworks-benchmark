from sanic import Sanic
from sanic import response
import asyncpg
import os

app = Sanic()


@app.listener('before_server_start')
async def register_db(app, loop):
    app.db = await asyncpg.create_pool(dsn=os.environ['DATABASE_URL'])


@app.listener('after_server_stop')
async def cleanup(app, loop):
    await app.db.close()


@app.route('/db')
async def handle_db(request):
    async with request.app.db.acquire() as connection:
        result = await connection.fetchval("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
    return response.html(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)