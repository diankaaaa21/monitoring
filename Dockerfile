
FROM python:3.12

RUN apt-get update && apt-get install -y build-essential libmariadb-dev



WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .

ENV DJANGO_SETTINGS_MODULE=monitoring.settings


EXPOSE 8000


RUN python manage.py migrate


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "monitoring.wsgi:application"]


