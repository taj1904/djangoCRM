# install mysal on your computer
# https://dev.mysql.com/downloads/installer/
# pip in stall mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='Monday1984'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE symbolica")

print('ALL DONE')
