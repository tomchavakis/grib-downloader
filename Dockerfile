FROM ubuntu:latest

WORKDIR /app

RUN apt-get -y update  && apt-get install -y python3 python3-pip curl

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]