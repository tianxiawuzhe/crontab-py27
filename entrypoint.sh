#!/bin/bash
set -x

today=`date +"%Y%m%d"`

appdir="/code"

printenv | sed 's/^\(.*\)$/export \1/g' | grep 'BIT_' > ${appdir}/project_env.sh
cat ${appdir}/project_env.sh

echo "copy time zone to localtime ..."
ls -l /var/spool/cron/crontabs/  ${appdir}/

cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

echo "restart contab services ..."
service cron restart

echo "entrypoint end "
#tail -f ${appdir}/jobs.log
