FROM python:3.9.2

COPY requirements.txt  ./
COPY main.py ./
COPY image_preprocessing.py ./
COPY predict.py ./

RUN apt update &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt

WORKDIR /app

CMD exec gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app