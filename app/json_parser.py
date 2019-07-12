import json
from string import maketrans
import re

class json_parser:
    def json_parse(self, data):
        json_string = json.dumps(data, ensure_ascii=False)
        json_string = re.sub("[\",:\[\]\\\\n\{]", "", json_string)
        messages = json_string.strip().split("}")
        messages = [message for message in messages if message]
        k = 0
        for message in messages:
            messages[k] = message.strip()
            k += 1

        return messages

