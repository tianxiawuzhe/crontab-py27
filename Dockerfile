FROM daocloud.io/python:2.7
MAINTAINER JiangLong <j_l2006@163.com>

RUN mkdir -p /code

WORKDIR /code

COPY . /code/
##COPY libs /usr/local/lib/python2.7/
ADD crontab_content.txt /var/spool/cron/crontabs/root

RUN apt-get update && \
apt-get install -y cron && \
apt-get install -y default-jre && \
apt-get install -y vim && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
touch /code/jobs.log && \
chmod +x /code/entrypoint.sh && \
chmod +x /code/cron_jobs.sh && \
chmod 0600 /var/spool/cron/crontabs/root && \
pip install --upgrade pip && \
pip install -r /code/requirements.txt && \
pip install easytrader==0.8.1 && \
apt-get clean && \
apt-get autoclean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
ls

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh"]
