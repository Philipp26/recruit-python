# -*- coding: utf-8 -*-
import sys
import os
from time_mod import time_handler

reload(sys)
sys.setdefaultencoding("utf-8")

class file_msg:
    def to_save_in_file(self, sender, time, message):
        if os.path.exists('message_logs.txt'):
            with open('message_logs.txt', "a") as txt:
                txt.write(u'{} - {} - {}\n'.format(sender, time, message).encode("utf-8"))
        else:
            with open('message_logs.txt',"w") as txt:
                txt.write(u'{} - {} - {}\n'.format(sender, time, message).encode("utf-8"))

    def prepare_for_save(self, messages):
        for message in messages:
            sender = message["sender"]
            time = time_handler().time_convert(message["time"])
            mess = message["message"]
            self.to_save_in_file(sender, time, mess)
