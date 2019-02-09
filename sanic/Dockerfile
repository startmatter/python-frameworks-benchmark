FROM python:3.7.2

ADD ./ /sanic

WORKDIR sanic

RUN pip3 install -r /sanic/requirements.txt

WORKDIR /sanic

EXPOSE 8080

ENTRYPOINT ["/sanic/conf/docker-entrypoint.sh"]

CMD gunicorn app:app --bind 0.0.0.0:8080 -c /sanic/conf/gunicorn.conf.py
 