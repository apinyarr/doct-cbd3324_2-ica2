FROM python:3.8.10-alpine3.14

WORKDIR /usr/src/app

ENV REDIS_HOST=localhost \
    REDIS_PORT=6379 \
    FLASK_APP="Visitor App"

COPY ["requirements.txt", "./"]

RUN pip install --no-cache -r requirements.txt

COPY ./app .

EXPOSE 5000

ENTRYPOINT ["python3", "./main.py"]