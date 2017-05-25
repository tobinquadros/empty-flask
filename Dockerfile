FROM python
MAINTAINER Tobin Quadros

COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt

CMD bin/start
