FROM python:3

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN mkdir static/files

EXPOSE 5000

CMD ["python", "app.py", "--host", "0.0.0.0"]
