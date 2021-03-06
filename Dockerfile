FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 9000

CMD python manage.py runserver 0.0.0.0:9000
