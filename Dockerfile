FROM continuumio/miniconda3
MAINTAINER Tobin Quadros

COPY . /code
WORKDIR /code

RUN conda install -c eklitzke pyflame
RUN pip install --no-cache-dir -r requirements.txt

CMD bin/start
