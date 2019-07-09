import pymysql
import json
from pymysql.cursors import DictCursor
from contextlib import closing
import os

class mysql_connector:
    def get_connect(self):
        path = r"/home/philipp/say1hello/recruit-python/settings/mysql_settings.json"
        with open(path) as json_settings:
            data =json.load(json_settings)

        connection = pymysql.connect(
            host = data['host'],
            port = data['port'],
            user = data['user'],
            password = data['password'],
            db = data["db"],
            charset = data["charset"],
            cursorclass = DictCursor)

        return connection

    def exec_query(self, query):
        with closing(self.get_connect()) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
