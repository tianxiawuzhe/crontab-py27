FROM daocloud.io/python:2.7
MAINTAINER JiangLong <j_l2006@163.com>

RUN mkdir -p /code

WORKDIR /code

COPY . /code/

RUN apt-get update && \
apt-get install -y cron && \
apt-get install -y default-jre && \
apt-get install -y vim && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
chmod 0600 /var/spool/cron/crontabs/root && \
pip install --upgrade pip && \
apt-get clean && \
apt-get autoclean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
ls

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "ls"]
