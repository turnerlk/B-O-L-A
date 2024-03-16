FROM python:latest

WORKDIR /app

COPY . .

RUN pip install django python-dotenv django-cors-headers PyJWT djangorestframework

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
