# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


import sqlite3


def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def create_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = """CREATE TABLE Student (
        Student_Id INTEGER NOT NULL,
        Student_Name TEXT NOT NULL,
        School_Id INTEGER NOT NULL PRIMARY KEY
        );"""
        cursor.execute(sqlquery)
        connection.commit()
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка при создании таблицы", error)


def insert_data():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = """INSERT INTO Student (Student_Id, Student_Name, School_Id)
        VALUES
        ('201', 'Иван', '1'),
        ('202', 'Петр', '2'),
        ('203', 'Анастасия', '3'),
        ('204', 'Игорь', '4');
        """
        cursor.execute(sqlquery)
        connection.commit()
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка при вставке данных", error)


def get_school_student(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sqlquery = """SELECT * FROM
            (SELECT Student.Student_Id, Student.Student_Name, Student.School_Id, School.School_Name
            FROM Student
            JOIN School ON Student.School_Id=School.School_Id)
        WHERE student_id = ?;
        """
        cursor.execute(sqlquery, (student_id,))
        record = cursor.fetchone()
        # print(record)
        print('ID Студента:', record[0])
        print('Имя студента:', record[1])
        print('ID школы:', record[2])
        print('Название школы:', record[3])
        connection.commit()
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Ошибка в получении данных", error)


# create_table()
# insert_data()
get_school_student('202')



