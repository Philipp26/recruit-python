import pymysql
import json
from pymysql.cursors import DictCursor
from contextlib import closing
import os

class mysql_connector:
    def get_connect(self):
        path = os.path.join(os.path.join('', 'settings'), "mysql_settings.json")
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

