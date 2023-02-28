import json
from datetime import datetime
from constants import BIOT_APP_NAME

logOptions = [
  { "function": "debug", "level": "DEBUG", "level_value": 10000 },
  { "function": "log", "level": "INFO", "level_value": 20000 },
  { "function": "info", "level": "INFO", "level_value": 30000 },
  { "function": "warn", "level": "WARN", "level_value": 40000 },
  { "function": "error", "level": "ERROR", "level_value": 50000 },
]

class logger:
    trace_id = "traceId-not-set"

    @classmethod
    def join_message(args):
        msg_str = ""
        for arg in args:
            msg_str += arg
        return msg_str
    
    @classmethod
    def print_log(cls, level, level_value, args):
        log_data = {
            "@timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "message": cls.join_message(args),
            "level": level,
            "level_value": level_value,
            "appName": BIOT_APP_NAME,
            "traceId": cls.trace_id,
        }
        print(json.dumps(log_data, indent=4))

    @classmethod
    def log(cls, *args):
        cls.print_log("INFO", 20000, args)

    @classmethod
    def debug(cls, *args):
        cls.print_log("DEBUG", 10000, args)

    @classmethod
    def info(cls, *args):
        cls.print_log("INFO", 30000, args)

    @classmethod
    def warn(cls, *args):
        cls.print_log("WARN", 40000, args)

    @classmethod
    def error(cls, *args):
        cls.print_log("ERROR", 50000, args)


