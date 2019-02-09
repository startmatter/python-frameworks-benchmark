from flask import Flask
import psycopg2
import os

app = Flask(__name__)
schema = 'schema.sql'
conn = psycopg2.connect(os.environ['DATABASE_URL'])

@app.route("/db")
def handle_db():
    with conn.cursor() as cursor2:
        cursor2.execute("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
        row = cursor2.fetchone()
    return row[0]

if __name__ == "__main__":
    app.run()
