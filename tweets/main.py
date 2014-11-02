from models import Tweeter
import os
import csv
import data
import sql_data

# Constants
ACCOUNTS_CSV = "accounts.csv"
DB_NAME = "database.db"
SCHEMA = "schema.sql"

# Absolute path to things
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ACCOUNTS_PATH = os.path.join(BASE_DIR, ACCOUNTS_CSV)
DB_PATH = os.path.join(BASE_DIR, DB_NAME)
SCHEMA_PATH = os.path.join(BASE_DIR, SCHEMA)


def load_accounts_csv():
    tweeters = data.load_accounts(ACCOUNTS_PATH)
    db = sql_data.Database(DB_PATH)
    db.init_db(SCHEMA_PATH)
    db.add_tweeters = tweeters
