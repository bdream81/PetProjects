import psycopg2
from psycopg2 import Error

try:
   
    conn = psycopg2.connect(
    dbname='my_pizza', 
    user='postgres', 
    password=123, 
    host='localhost'
)


    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM zavtrak"

    cursor.execute(postgreSQL_select_Query)
    zavtrak = cursor.fetchall()
 
    for row in zavtrak:
        print("nazvanie =", row[1], )
        print("put_do_photo =", row[2])
        print("price =", row[3], "\n")
    print("-"*50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM pizza40"

    cursor.execute(postgreSQL_select_Query)
    pizza40 = cursor.fetchall()
 
    for row in pizza40:
        print("nazvanie =", row[1], )
        print("put_do_photo =", row[2])
        print("price =", row[3], "\n")
    print("-"*50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM rolly"

    cursor.execute(postgreSQL_select_Query)
    rolly = cursor.fetchall()
 
    for row in rolly:
        print("nazvanie =", row[1], )
        print("put_do_photo =", row[2])
        print("price =", row[3], "\n")
    print("-"*50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM salaty"

    cursor.execute(postgreSQL_select_Query)
    salaty = cursor.fetchall()
 
    for row in salaty:
        print("nazvanie =", row[1], )
        print("put_do_photo =", row[2])
        print("price =", row[3], "\n")
    print("-"*50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM zakuski"

    cursor.execute(postgreSQL_select_Query)
    zakuski = cursor.fetchall()
 
    for row in zakuski:
        print("nazvanie =", row[1], )
        print("put_do_photo =", row[2])
        print("price =", row[3], "\n")
    print("-"*50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM aksii"

    cursor.execute(postgreSQL_select_Query)
    aksii = cursor.fetchall()
 
    for row in aksii:
        print("nazvanie =", row[1], )
        print("put_do_photo =", row[2])
        print("opisanie =", row[3], "\n")
    print("-"*50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM vacancy"

    cursor.execute(postgreSQL_select_Query)
    vacancy = cursor.fetchall()
 
    for row in vacancy:
        print("nazvanie =", row[1], )
        print("opisanie =", row[2], "\n")
    print("-" * 50)

    cursor = conn.cursor()
    postgreSQL_select_Query = "SELECT * FROM o_nas"

    cursor.execute(postgreSQL_select_Query)
    o_nas = cursor.fetchall()
 
    for row in o_nas:
        print("opisanie =", row[1], "\n")


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")
