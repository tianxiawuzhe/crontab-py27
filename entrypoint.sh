#!/bin/bash
today=`date +"%Y%m%d"`

appdir="/code"

##������������Ҫ�����ݿ����ӵĻ������������޸ĳɱ����Լ��Ļ���������Ϣ
printenv | sed 's/^\(.*\)$/export \1/g' | grep 'BIT_' > ${appdir}/project_env.sh
cat ${appdir}/project_env.sh

cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

service cron restart

tail -f ${appdir}/jobs.log
