import pymysql
import pymysql.cursors
import pandas as pd
import hashlib
import json
from threading import Lock


def QueryWithConnect(s):
    db = pymysql.connect(host='localhost', user='root',
                         password='123456', database='arknights', port=3306)
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute(s)
    res = cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    return res


class MySQL:
    def __init__(self, host='localhost', user='root', pwd='123456', database='arknights'):
        self.db = pymysql.connect(
            host=host, user=user, password=pwd, database=database, port=3306)
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        self.lock = Lock()
        # 在初始化的时候获取一次数据
        # self.data = self.getDataFromTable('paints').to_json(force_ascii=False, orient='table')

    def addUser(self, username, password, email, phone):
        try:
            sql_cmd = "INSERT INTO `user_info` VALUES ('{}','{}','{}','{}','1','能天使','能天使');".format(
                username, password, email, phone)
            self.cursor.execute(sql_cmd)
            self.db.commit()
            return True
        except:
            return False

    def hasUser(self, username, password):
        try:
            sql_cmd = "SELECT * FROM user_info WHERE ID = '{}' and password = '{}';".format(
                username, password)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchone()
            if res:
                return True
            else:
                return False
        except:
            return False

    # 查询用户名是否存在
    def verifyID(self, ID):
        sql_cmd = "SELECT * FROM user_info WHERE ID = '{}';".format(ID)
        self.lock.acquire()
        self.cursor.execute(sql_cmd)
        res = self.cursor.fetchone()
        self.lock.release()
        if res:
            return True
        else:
            return False


    def getSkins(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM skin_info WHERE skin_operator_name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchall()
            return res
        except:
            rese = []
            return rese

    def getVoices(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM voice_info WHERE voice_operator_name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchall()
            return res
        except:
            rese = []
            return rese

    def getDetails(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM details_info WHERE details_operator_name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchone()
            return res
        except:
            rese = []
            return rese

    def getBaseinfo(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM operator_base_info WHERE name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchone()
            return res
        except:
            rese = {}
            return rese

    def getAttribute(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM operator_attribute_info WHERE operator_name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchone()
            return res
        except:
            rese = {}
            return rese


    def getSkills(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM skill_info WHERE operator_name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchall()
            return res
        except:
            rese = []
            return rese

    def searchOperator(self, operator_name):
        try:
            sql_cmd = "SELECT * FROM operator_base_info WHERE name = '{}';".format(operator_name)
            self.cursor.execute(sql_cmd)
            res = self.cursor.fetchone()
            if res:
                return True
            return False
        except:
            return False










