FROM python:3.7.2

ADD ./ /fastapi

WORKDIR fastapi

RUN pip3 install -r /fastapi/requirements.txt

WORKDIR /fastapi

EXPOSE 8080

ENTRYPOINT ["/fastapi/conf/docker-entrypoint.sh"]

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
 