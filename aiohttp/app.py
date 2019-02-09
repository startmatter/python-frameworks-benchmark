import asyncio
import asyncpg
from aiohttp import web
import os
import uvloop


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def handle_db(request):
    """Handle incoming requests."""
    db = request.app['db']

    # Take a connection from the pool.
    async with db.acquire() as connection:
        # Open a transaction.
        # async with connection.transaction():
            # Run the query passing the request argument.
        result = await connection.fetchval("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
    return web.Response(text=result, content_type='text/html')


async def init_app():
    """Initialize the application server."""
    app = web.Application()
    app['db'] = await asyncpg.create_pool(dsn=os.environ['DATABASE_URL'])
    app.router.add_route('GET', '/db', handle_db)
    return app
