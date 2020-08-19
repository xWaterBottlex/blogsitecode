FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ADD ./app /app
WORKDIR /app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN pip install -r requirements.txt

CMD ["python3", "webapp.py"]