#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import threading, time, traceback, json
from dbutil import DbUtil
from QYWeiXin import QYWeixinMsg
import Util

appdir = os.path.dirname(os.path.abspath(__file__)) + '/app'
if os.path.exists(appdir):
    sys.path.append(appdir)

class Task(object):  
    def __init__(self,id, mod,cls,func, cycle, run_cnt, args=None):
        self.id = id 
        self.mod = mod
        self.cls = cls
        self.func = func
        self.cycle = cycle
        self.cnt = run_cnt
        self.args = args
        
    def __call__(self):
        ## 先设置正在执行中状态，以免下次线程启动执行
        with DbUtil() as c1:
            c1.execute("UPDATE job_task set status=3 where id=%d" % self.id)
        try:
            ## 开始执行
            for i in range(self.cnt):
                m = __import__(self.mod)
                if self.cls is None or self.cls == "":
                    f = getattr(m, self.func)
                    f() if self.args is None else f(self.args)
                else:
                    c = getattr(m, self.cls)
                    obj = c()
                    getattr(obj, self.func)() if self.args is None else getattr(obj, self.func)(self.args)
                time.sleep(self.cycle)
            with DbUtil() as c2:
                sql = "UPDATE job_task set run_time=DATE_ADD(run_time, "\
                    " INTERVAL DATEDIFF('%s', run_time)+1 DAY) "\
                    " WHERE id=%d" % (Util.get_now_time(), self.id)
                cnt = c2.execute(sql)
        except Exception as exp:
            traceback.print_exc()
            Util.echo("Error: task ", self.mod, self.cls, self.func, self.cycle, self.args, repr(exp))
        finally:
            with DbUtil() as c3:
                c3.execute("UPDATE job_task set status=1 where id=%d" % self.id)

if __name__ == '__main__':
    try:
        Util.echo("jobs begin ...")
        res = None
        with DbUtil() as cur:
            cur.execute("select id, mod_name, cls_name, fuc_name, args, run_time, cycle, run_cnt, status from job_task \
                where status=1 and run_time<'%s'" % (Util.get_now_time()))
            res = cur.fetchall()
        for row in res:
            Util.echo("start task:", row)
            args = None if row['args']=='' else json.loads(row['args'])
            t = threading.Thread(target=Task(row['id'], row['mod_name']
                , row['cls_name'], row['fuc_name'], row['cycle'], row['run_cnt'], args))
            t.start()
    except Exception as exp:
        Util.echo(repr(exp))
        traceback.print_exc()
        w = QYWeixinMsg()
        if not w.sendMsg(u"%s" % repr(exp)):
            Util.echo("connect to weixin failed.")
