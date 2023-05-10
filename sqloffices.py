import psycopg2
from infodata import host, user, password, db_name
import json


with open("offices.json", "r") as file:
    data = json.load(file)

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    # with connection.cursor() as cursor:
    #     cursor.execute("""CREATE TABLE offices(
    #     id serial PRIMARY KEY,
    #     Parentid integer,
    #     Name varchar(255) NOT NULL,
    #     Type integer NOT NULL);""")
    #
    # with connection.cursor() as cursor:
    #     insert_script = 'INSERT INTO offices (Parentid, Name, Type) VALUES (%s, %s, %s)'
    #     for office in data["offices"]:
    #         cursor.execute(insert_script, (office["ParentId"], office["Name"], office["Type"]))

    # with connection.cursor() as cursor:
    #     cursor.execute(""" DROP TABLE offices;""")

except Exception as ex:
    print(ex)

else:
    connection.close()
    print("table close")