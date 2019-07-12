from datetime import datetime
import re
class time_handler:
    def time_array_convert(self, arr):
        start_time = time_convert(arr[0])
        end_time = time_convert(arr[-1])

        if len(arr) == 1:
            return (start_time)

        return (start_time, end_time)

    def time_convert(self, time):
        return datetime.utcfromtimestamp(float(time)).strftime("%d.%m.%Y %H:%M:%S")

    def get_timestamp_dates(self, messages):
        dates = []

        for message in messages:
            dates.append(message["time"])

        return dates
