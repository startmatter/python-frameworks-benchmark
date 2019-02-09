from django.http import HttpResponse
from django.db import connection


def handle_db(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT html FROM render_cache_pagehtml WHERE url='startmatter.com'")
        row = cursor.fetchone()
    return HttpResponse(row[0])
