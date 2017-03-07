#!/bin/bash
today=`date +"%Y%m%d"`

appdir="/code"

##环境变量，主要是数据库连接的环境变量，需修改成本地自己的环境变量信息
printenv | sed 's/^\(.*\)$/export \1/g' | grep 'BIT_' > ${appdir}/project_env.sh
cat ${appdir}/project_env.sh

cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

service cron restart

tail -f ${appdir}/jobs.log
