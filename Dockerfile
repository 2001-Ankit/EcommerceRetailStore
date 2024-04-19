FROM python:3.13-rc-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirement.txt requirement.txt

RUN pip3 install -r requirement.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000