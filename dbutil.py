# coding: utf-8
import sys, os
import Util
import MySQLdb
import MySQLdb.cursors

class DbUtil:
    __config = None
    __con = None
    __cur = None
    
    ####
    def __init__(self):
        cfg = Util.file2dict(os.path.dirname(os.path.abspath(__file__)) + '/config/global.json')
        if cfg and cfg["DBConnect"]:
            self.__config = cfg["DBConnect"]
        
        self.__con = MySQLdb.connect(
            host   = os.getenv(self.__config["host"]),
            port   = int(os.getenv(self.__config["port"])),
            user   = os.getenv(self.__config["user"]),
            passwd = os.getenv(self.__config["pswd"]),
            db     = os.getenv(self.__config["name"]),
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            connect_timeout = 30
        )
        self.__con.autocommit(1)
        self.__cur = self.__con.cursor()

    def __enter__(self):
        return self.__cur
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_tb is None and self.__cur is not None:
            self.__con.commit()
            self.__cur.close()
            self.__con.close()
            return True
        else:
            return False

