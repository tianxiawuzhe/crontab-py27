FROM daocloud.io/python:2.7
MAINTAINER JiangLong <j_l2006@163.com>

RUN mkdir -p /code

WORKDIR /code

COPY . /code/


EXPOSE 8000

#ENTRYPOINT ["/bin/bash", "ls"]
