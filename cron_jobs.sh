#!/bin/bash

appdir="/code/"

log="${appdir}/jobs.log"

source ${appdir}/project_env.sh 1>> ${log} 2>&1
/usr/local/bin/python ${appdir}/jobs.py 1>> ${log} 2>&1
