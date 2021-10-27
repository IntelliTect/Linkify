import mysql.connector
from mysql.connector import errorcode
from mysql.connector.connection import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from .env import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


class Connection():
    connection: MySQLConnection
    cursor: MySQLCursor

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=3306,
                database=DB_NAME,
                use_pure=True,
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Something is wrong with the user name or password") from err
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist") from err
            raise
        else:
            self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.cursor._have_unread_result():
            self.cursor.reset()
        self.cursor.close()
        self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, _, __, ___):
        self.disconnect()

