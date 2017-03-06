#!/bin/bash
today=`date +"%Y%m%d"`

printenv | sed 's/^\(.*\)$/export \1/g' | grep 'BIT_' > /code/project_env.sh
cat /code/project_env.sh
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
service cron restart

tail -f /code/jobs.log
