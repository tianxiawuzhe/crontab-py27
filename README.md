# crontab-py27
* �������daocloud.io/python:2.7
* ����һ��crontab����ʹ�����ݿ���ƶ�ʱ����
* �����а�װvim����

## �ļ�˵��
* app/config/global.json�������ļ����������ݿ����Ӽ�΢����ҵ�ŵ�����
* QYWeiXin.py��΢����Ϣ����ģ�飬��ȡapp/config/global.json������
* Util.py��ͨ�õĹ��ܣ�������ӡ��־����ȡʱ�䣬��ȡ�����ļ��Ȼ�������
* create_table.txt���������ݿ���SQL���
* crontab_content.txt����docker�������crontab����
* cron_jobs.sh��[crontab_content.txt]��ָ��������ű�
* jobs.py��[cron_jobs.sh]�ű�����Ҫʹ�õ��Ķ��߳̽ű�����ʱ������ݿ��Ƿ��з��ϵ���������У����½��̲߳�ִ��
* dbutil.py�����ݿ����ӵĹ��ýű�
* entrypoint.sh��docker�����������״�ִ�еĽű�
```shell
ע������и�tail -f�����������Ϊ�˱�֤���������Զ��˳������������������󣬵�ִ����[entrypoint.sh]������Ҳ�������˳���
```
* Dockfile�����reqirements.txt���а����������籾����easytrader��������Ѵ˰�����Dockfile�а�װ��ԭ��Ϊreqirements.txt��װʱ������ȫ��������������Ȼ���ٽ��а�װ��������ĳ��������û�а�װ�����ֱ�ӱ�������reqirmentsҲ�Ͱ�װ���ɹ���

## ����
* �����̽���Ϊdocker��python2.7�����������ݿⷽʽ���Ƶĵ�������������ڴ˻����Ͻ����ٴ��޸���չ�������㲻ͬ����
