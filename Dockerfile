FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
COPY test_task_quintagroup ./