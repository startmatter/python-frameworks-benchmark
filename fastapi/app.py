import asyncpg
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
async def register_db():
    app.db = await asyncpg.create_pool(dsn=os.environ['DATABASE_URL'])


@app.on_event("shutdown")
async def cleanup():
    await app.db.close()


@app.get('/db')
async def handle_db():
    async with app.db.acquire() as connection:
        result = await connection.fetchval("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
    return result



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)