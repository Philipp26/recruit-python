# -*- coding: utf-8 -*-
from sql_query import sql_query
from file_mod import file_msg
from time_mod import time_handler
import json

class App:
    def show(self, environ, start_response):
        status = '200 OK'

        sql =sql_query()

        message_logs = sql.select_query("dialogs", ["start_time", "end_time", "message_count"])

        result = self.represent_response(message_logs)

        start_response(status, [
            ('Content-Type', 'text/plain;charset=utf-8'),
            ('Content-Length', str(len(result)))
        ])

        return [result]

    def save(self, environ, start_response):
        status = '200 OK'
        length = int(environ['CONTENT_LENGTH'])

        body = environ['wsgi.input'].read(length).decode('utf-8')
        messages = json.loads(body)

        file_msg().prepare_for_save(messages)

        sql = sql_query()

        time_hdlr = time_handler()

        message_data = time_hdlr.get_timestamp_dates(messages)

        sql.insert_query("dialogs", ["start_time", "end_time", "message_count"], [str(message_data[0]),str( message_data[-1]), str(len(message_data))])

        start_response(status, [('Content-Length', '0')])

        return [b'']

    def represent_response(self, messages):
        count = 1
        result = ''
        time_hdlr = time_handler()
        for message in messages:
            result = result + '''Запись {}: Сообщений - {} шт с {} по {}\n'''.format(count, message["message_count"],
                     time_hdlr.time_convert(message["start_time"]),
                     time_hdlr.time_convert(message["end_time"]))
            count += 1
        return result


