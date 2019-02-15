FROM python:3.7.2

ADD ./ /aiohttp

WORKDIR aiohttp

RUN pip3 install -r /aiohttp/requirements.txt

WORKDIR /aiohttp

EXPOSE 8080

ENTRYPOINT ["/aiohttp/conf/docker-entrypoint.sh"]

CMD ["python3", "/aiohttp/app.py"]