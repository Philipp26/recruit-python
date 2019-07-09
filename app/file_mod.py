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
                txt.write('{} - {} - {}\n'.format(sender, time, message))
        else:
            with open('message_logs.txt',"w") as txt:
                txt.write('{} - {} - {}\n'.format(sender, time, message))

    def prepare_for_save(self, messages):
        for message in messages:
            items_of_message = message.split("    ")
            if len(items_of_message) > 1:
                sender = items_of_message[1].split(' ')[1]
                time = time_handler().time_convert(items_of_message[0].split(' ')[1])
                mess = items_of_message[2].split(' ')[1::]
                mess = ' '.join(mess)

                self.to_save_in_file(sender, time, mess)
