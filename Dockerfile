FROM daocloud.io/python:2.7
#FROM daocloud.io/longsir/stock:master-f4a0fed
MAINTAINER JiangLong <j_l2006@163.com>

RUN mkdir -p /code

WORKDIR /code

COPY . /code/
COPY libs /usr/local/lib/python2.7/
ADD cron_stock.txt /var/spool/cron/crontabs/root

RUN apt-get update && \
apt-get install -y cron && \
apt-get install -y default-jre && \
apt-get install -y vim && \
touch /code/jobs.log && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
chmod +x /code/entrypoint.sh && \
chmod +x /code/cron_jobs.sh && \
chmod 0600 /var/spool/cron/crontabs/root && \
pip install --upgrade pip && \
pip install -r /code/requirements.txt && \
pip install easytrader && \
apt-get clean && \
apt-get autoclean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
ls

#pip install -r /code/libs/easytrader/requirements.txt && \
#chown -R app:crontab /var/spool/cron/crontabs/app && \
#chmod 600 /var/spool/cron/crontabs/app && \

#EXPOSE 8000

ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh"]
