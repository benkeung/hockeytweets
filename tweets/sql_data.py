import os
import sqlite3

class Database(object):

    def __init__(self, db_name):
        self.__connection = sqlite3.connect(db_name)

    def add_tweeters(self, tweeters):
        tweeters_tuple = [t.convert_to_sql_tuple() for t in tweeters]

        cur = self.__connection.cursor()
        cur.executemany(
            "INSERT OR IGNORE INTO tweeters VALUES (?,?,?,?,?)", tweeters_tuple)
        self.__connection.commit()
        s = cur.fetchall()
        print s

    def init_db(self, db_file):
        with open(db_file) as f:
            cur = self.__connection.cursor()
            s = f.read()
            cur.executescript(s)
        self.__connection.commit()

    def close(self):
        self.__connection.close()
