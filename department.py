import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'Ireallyhopeso.79',
    'host': 'localhost',
    'database': 'library'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

DB_NAME = 'library'

TABLES = {}

TABLES['department'] = (
    "CREATE TABLE `department` ("
    " `deptId` int NOT NULL AUTO_INCREMENT,"
    " `deptName` varchar(250) NOT NULL,"
    " PRIMARY KEY (`deptId`)"
    ") ENGINE=InnoDB"
)
def create_database():
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    print("Database {} created!".format(DB_NAME))


def create_tables():
    cursor.execute("USE {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({}) ".format(table_name), end="")
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exists")
            else:
                print(err.msg)

create_database()
create_tables()
