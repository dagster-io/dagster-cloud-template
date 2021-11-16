FROM python:3.8-slim

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

RUN pip install -e .
