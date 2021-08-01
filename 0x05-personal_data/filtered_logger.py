#!/usr/bin/env python3
""" filter_datum  module
"""
import os
import logging
import mysql.connector
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ INIT
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values in incoming log records.
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns the log message obfuscated"""
    for field in fields:
        message = re.sub(
            '(?<={}=)[^{}]*'.format(field, separator), redaction, message)
    return message


def get_logger() -> logging.Logger:
    """ Create logger
    """
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    stream = logging.StreamHandler()
    frm = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(frm)
    log.addHandler(stream)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ 
    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME")
    pw = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    db = os.getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(user=user, password=pw,
                                   host=host, database=db)


def main():
    """retrieve all rows in the users table
    and display each row under a filtered format.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    result = cursor.fetchall()
    for data in result:
        message = "name={}; email={}; phone={}; ssn={}; password={}; \
ip={}; last_login={}; user_agent={};".format(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5],
            data[6],
            data[7])
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
