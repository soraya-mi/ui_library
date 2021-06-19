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

TABLES['book_isbn'] = (
    "CREATE TABLE `book_isbn` ("
    " `isbn` int NOT NULL AUTO_INCREMENT,"
    " `title` varchar(250) NOT NULL,"
    " `author` varchar(250) NOT NULL,"
    " `publisher` varchar(250) NOT NULL,"
    " PRIMARY KEY (`isbn`)"
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

def add_book_isbn(isbn,title,author,publisher):
    sql = ("INSERT INTO book_isbn(isbn,title,author,publisher) VALUES (%s, %s, %s, %s)")
    cursor.execute(sql, (isbn,title,author,publisher))
    db.commit()
    book_isbn_id = cursor.lastrowid
    print("Added bbok isbn {}".format(book_isbn_id))


# def get_logs():
#     sql = ("SELECT * FROM logs ORDER BY created DESC")
#     cursor.execute(sql)
#     result = cursor.fetchall()
#
#     for row in result:
#         print(row[1])
#
#
# def get_log(id):
#     sql = ("SELECT * FROM logs WHERE id = %s")
#     cursor.execute(sql, (id,))
#     result = cursor.fetchone()
#
#     for row in result:
#         print(row)
#
#
# def update_log(id, text):
#     sql = ("UPDATE logs SET text = %s WHERE id = %s")
#     cursor.execute(sql, (text, id))
#     db.commit()
#     print("Log updated")
#
#
# def delete_log(id):
#     sql = ("DELETE FROM logs WHERE id = %s")
#     cursor.execute(sql, (id,))
#     db.commit()
#     print("Log removed")
#
# add_log('This is log one', 'Brad')
# add_log('This is log two', 'Jeff')
# add_log('This is log three', 'Jane')
add_book_isbn(1,"hi","me","me_again")
# get_logs()
# get_log(2)

# update_log(2, 'Updated log')

# delete_log(2)
# delete_log(2)
# delete_log(5)
# get_logs()