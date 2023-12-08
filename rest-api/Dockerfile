# FROM python:latest
FROM python:3.11.7-slim-bullseye

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python3 ./main.py
