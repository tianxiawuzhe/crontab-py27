# coding: utf-8
import sys, os, time
import logging
import six, json
#from bae_log import handlers

mylogger = None

if six.PY2:
    from io import open
    
def get_now_time(fmt='%Y-%m-%d %H:%M:%S'):
    return time.strftime(fmt, time.localtime(time.time()))

def echo(*args):
    print('%s: %r'%(get_now_time(), args))

def file2dict(path):
    ret = None
    try:
        with open(path, encoding='utf-8') as f:
            ret = json.load(f)
        for v in ret:
            if type(v) is int:
                echo("config's value should be string, or unknown exception will be shown.")
    except Exception as exp:
        echo('read file error:', exp)
    return ret
    