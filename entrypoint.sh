#!/bin/bash

today=`date +"%Y%m%d"`

appdir="/code"

printenv | sed 's/^\(.*\)$/export \1/g' | grep 'BIT_' > ${appdir}/project_env.sh
##cat ${appdir}/project_env.sh
ls -l /var/spool/cron/crontabs/  ${appdir}/
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
#service cron restart

#tail -f ${appdir}/jobs.log
