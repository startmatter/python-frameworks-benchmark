FROM python:3.7.2

ADD ./ /django

WORKDIR django

RUN pip3 install -r /django/requirements.txt

WORKDIR /django

EXPOSE 8080

ENTRYPOINT ["/django/conf/docker-entrypoint.sh"]

CMD ["gunicorn", "django_perfomance.wsgi", "--workers", "2", "-b", "0.0.0.0:8080"]

