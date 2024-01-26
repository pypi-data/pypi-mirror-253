import os
from dotenv import load_dotenv

load_dotenv()

def to_bool(value):
    """
       Converts 'something' to boolean. Raises exception for invalid formats
           Possible True  values: 1, True, "1", "TRue", "yes", "y", "t"
           Possible False values: 0, False, None, [], {}, "", "0", "faLse", "no", "n", "f", 0.0, ...
    """
    if str(value).lower() in ("True", "yes", "y", "true",  "t", "1"): return True
    if str(value).lower() in ("False", "no",  "n", "false", "f", "0", "0.0", "", "none", "[]", "{}"): return False
    raise Exception('Invalid value for boolean conversion: ' + str(value))

ENVIRONMENT_DEBUG = to_bool(os.environ.get("TIMEKEEPER_DEBUG", False))
ENVIRONMENT_PORT = os.environ.get("TIMEKEEPER_PORT", 5000)
DB_DATABASE = os.environ.get("DB_DATABASE", "employee")
DB_USERNAME = os.environ.get("DB_USERNAME", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = os.environ.get("DB_PORT", 5432)
REDIS_HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
SYNC_RUNNER = to_bool(os.environ.get("SYNC_RUNNER", False))