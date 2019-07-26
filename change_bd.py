import  mysql.connector
import conf

from mysql.connector import Error

# Сохранение информации о людях


def connection():
    try:
        con = mysql.connector.connect(host=conf.host,
                                  database=conf.database,
                                  user=conf.user,
                                  password=conf.pas)
    except Error as e:
        print(e)
    return con

def insert_person(name, last_name, phone, sex):
    try:
        con = connection()
        if con.is_connected():
                cursor = con.cursor()
                query = ("INSERT INTO PERSON_LIST(name,last_name,phone,sex) VALUES('%s','%s','%s','%s')") % (name, last_name, phone, sex)
                cursor.execute(query)
                con.commit()
    except Error as e:
            print(e)
    finally:
            con.close()

# Запрос на количество записей в БД
def count():
    try:
        con = con = connection()
        if con.is_connected():
                cursor = con.cursor()
                query = ("SELECT count(*) from PERSON_LIST")
                cursor.execute(query)
                result = cursor.fetchone()

                for i in result:
                    return i
    except Error as e:
            print(e)
    finally:
            con.close()

# Запрос для выборку из БД
def selct_table():
    try:
        con = connection()
        if con.is_connected():
                cursor = con.cursor()
                query = ("SELECT name, last_name, phone, sex from PERSON_LIST")
                cursor.execute(query)
                result = cursor.fetchall()
                return result
    except Error as e:
            print(e)
    finally:
            con.close()

# Удаление
def delete_person(person):

    try:
        con = connection()
        if con.is_connected():
                cursor = con.cursor()
                query = ("DELETE FROM PERSON_LIST WHERE name='%s' and last_name='%s' and phone='%s' and sex='%s'")%(person[0], person[1], person[2], person[3])
                cursor.execute(query)
                con.commit()
    except Error as e:
            print(e)
    finally:
            con.close()

# Изминение информации в ячейках
def update_cell(person, cellText, column):
    print(person)
    if column == 0:
        a = 'name'
    if column == 1:
        a = 'last_name'
    if column == 2:
        a = 'phone'
    if column == 3:
        a = 'sex'
    try:
        con = connection()
        if con.is_connected():
                cursor = con.cursor()
                select_query = ("SELECT id FROM PERSON_LIST WHERE name = '%s' and last_name = '%s' and phone = '%s' and sex = '%s'")%(person[0],person[1], person[2], person[3])
                cursor.execute(select_query)
                result = cursor.fetchone()
                for tmp in result:
                    rlt = tmp
                query = ("UPDATE PERSON_LIST SET %s = '%s' WHERE id = '%s'")%(a, cellText, rlt)
                cursor.execute(query)
                con.commit()

    except Error as e:
            print(e)
    finally:
            con.close()