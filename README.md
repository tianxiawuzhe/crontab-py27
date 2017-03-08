# py27-cron-weixin
* 镜像基于daocloud.io/python:2.7
* 建立一条crontab任务，使用数据库控制定时调度
* 含给微信企业号发送消息

## 文件说明
* config/global.json：配置文件，包括数据库连接及微信企业号的配置
* QYWeiXin.py：微信消息发送模块，读取global.json的配置
* Util.py：通用的功能，包括打印日志，获取时间，读取配置文件等基本功能
* create_table.txt：建立数据库表的SQL语句
* crontab_content.txt：在docker容器里的crontab任务
* cron_jobs.sh：[crontab_content.txt]中指明的任务脚本
* jobs.py：[cron_jobs.sh]脚本中需要使用到的多线程脚本，定时检查数据库是否有符合的任务，如果有，就新建线程并执行
* dbutil.py：数据库连接的公用脚本
* entrypoint.sh：docker容器启动后首次执行的脚本。
 * 最后有个tail -f命令，防止容器不自动退出。docker容器启动时若启动脚本会自行执行完，则容器也会跟着自行退出。
* Dockfile：如果reqirements.txt中有包的依赖（如本文中easytrader），则需把此包放在Dockfile中安装。原因为reqirements.txt安装时，会先全部检查包的依赖，然后再进行安装；如果检查某包的依赖没有安装，则会直接报错，整个reqirments也就安装不成功。

## 其他
* 本工程仅作为docker中python2.7及启动以数据库方式控制的调度任务管理，可在此基础上进行再次修改扩展，以满足不同需求
