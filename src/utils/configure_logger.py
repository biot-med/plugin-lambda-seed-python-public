import json
from datetime import datetime
from src.constants import BIOT_APP_NAME

class logger:
    trace_id = "traceId-not-set"

    @classmethod
    def join_message(cls, args):
        msg_str = ""
        for arg in args:
            msg_str += str(arg)
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

    @classmethod
    def configure_logger(cls, trace_id):
        cls.trace_id = trace_id


