FROM python:3.8.5

WORKDIR /code
COPY requirements.txt .
RUN pip install -r ./requirements.txt
RUN apt-get update
RUN apt-get install vim
RUN apt-get install wkhtmltopdf
COPY . .
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000