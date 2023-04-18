FROM python:3.9.15

WORKDIR /
COPY src/requirements.txt src/requirements.txt
RUN pip install -r src/requirements.txt

COPY ./src /src
WORKDIR /src

CMD python manage.py collectstatic --noinput && python manage.py migrate  && daphne -b 0.0.0.0 -p 8000 bookstore.asgi:application
 
