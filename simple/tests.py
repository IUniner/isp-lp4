from django.test import TestCase

# Create your tests here.

# import psycopg2
# import psycopg2.extras
# from config import Config
#
# # POSTGRES_NAME = "BotDB"
# # POSTGRES_USER = "BotUser"
# # POSTGRES_PASS = "BotPassword"
# # POSTGRES_HOST = "0:8000"
#
# # POSTGRES_NAME = "test_database"
# # POSTGRES_USER = "postgres"
# # POSTGRES_PASS = "test_password"
# # POSTGRES_HOST = "localhost:5432"
#
# # conn = psycopg2.connect(host="localhost", port="5432", database="test_database", user="postgres", password="test_password")
# # conn = psycopg2.connect("dbname=test_database user=tester password=test_password port=5432")
# # conn = psycopg2.connect("port=5432 dbname=test_database user=postgres password=test_password")
#
# # cur = conn.cursor()
# # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# # cur.execute("CREATE TABLE student (id SERIAL PRImARY KEY, name VARCHAR);")
# # cur.execute("INSERT INTO student (name) VALUES(%s)", ("Cristina",))
# # cur.execute("SELECT * FROM student;")
# # print(cur.fetchall())
#
# # with conn:
# #     with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#
#         # cur.execute("SELECT FROM student WHERE id = %s;", (1,))
#
#         # cur.execute("SELECT * FROM student;")
#         # print(cur.fetchall())
#
# #         print(cur.fetchone()['name'])
# #         cur.execute("INSERT INTO student (name) VALUES(%s)", ("David",))
# # conn.commit()
# # cur.close()
#
# # conn.close()
#
#
# def connect():
#     connection = None
#     try:
#         params = Config()
#         print('Connecting to the PostgreSQL db...')
#         connection = psycopg2.connect(**params)
#         """
#         Create a cursor.
#         """
#         cursor = connection.cursor()
#         print('PostgreSQL db version: ')
#         cursor.execute('SELECT version()')
#         db_version = cursor.fetchone()
#         print(db_version)
#     except(Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if connection is not None:
#             connection.close()
#             print('Db connection terminated.')
#
#
# connect()
