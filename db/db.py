from peewee import MySQLDatabase

from data import MYSQL_DATABASE,MYSQL_USER,MYSQL_HOST,MYSQL_PASSWORD


db = MySQLDatabase(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    database=MYSQL_DATABASE,
    )