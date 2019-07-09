from db_connector import mysql_connector
from pymysql.cursors import DictCursor
from contextlib import closing

class sql_query:
    def __init__(self):
        self.mysql = mysql_connector()

    def exec_query(self, query):
        with closing(self.mysql.get_connect()) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()

    def exec_query_return(self, query):
        with closing(self.mysql.get_connect()) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def insert_query(self, table, fileds, values):
        self.exec_query('''INSERT INTO {} ({})
        values ({})'''. format(table, ", ".join(fileds), ", ".join(values)))

    def select_query(self, table, fileds):
        return self.exec_query_return('''select {} FROM  {}
        '''. format(", ".join(fileds), table))

