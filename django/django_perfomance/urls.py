from django.conf.urls import url
from django.contrib import admin
from django_perfomance.views import handle_db

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^db/', handle_db),
]
