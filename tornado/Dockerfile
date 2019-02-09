FROM python:3.7.2

ADD ./ /tornado

WORKDIR tornado

RUN pip3 install -r /tornado/requirements.txt

WORKDIR /tornado

EXPOSE 8080

ENTRYPOINT ["/tornado/conf/docker-entrypoint.sh"]

CMD gunicorn -k tornado app:app -c /tornado/conf/gunicorn.conf.py