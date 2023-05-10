import psycopg2
from infodata import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    request = input("Введите цифру 3: ")
    list_of_trash = []
    list_of_slaves = []

    with connection.cursor() as cursor:
        cursor.execute(
            f"""with recursive temp1 ("id", parentid, "name", "type", path) as (
            select t1.id, t1.parentid, t1.name, t1.type, cast (t1.name as varchar(100)) as path
            from offices t1 where t1.type = \'{request}\'
            union
            select t2.id, t2.parentid, t2.name, t2.type, cast (temp1.path || '->' || t2.name as varchar(100))
            from offices t2 join temp1 on (temp1.parentid = t2.id))
            select * from temp1;""")

        for i in cursor.fetchall():
            for j in i:
                if j == "Офис в Санкт-Петербурге":
                    list_of_trash.append(i)

        for i in list_of_trash:
            list_of_slaves.append(i[4].partition("-")[0])

        print(list_of_slaves)


except Exception as ex:
    print(ex)

else:
    connection.close()
