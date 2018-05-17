import pymysql

from hrs import Dept


def main():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'hrs',
        'port': 3306,
        'charset': 'utf8',
        'autocommit': False,
        'cursorclass': pymysql.cursors.DictCursor  # cursorclass设置cursor游标的类型)
    }
    conn = pymysql.connect(**config)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'select dno no, dname name, dloc loc from tbdept')
            result = cursor.fetchone()
            while result:
                # 关系型数据库 - 关系模型
                # Python程序 - 对象模型
                # ORM - Object Relation Mapping - Alchemy
                # 有了ORM以后操作数据库就再也不用写SQL
                dept = Dept(**result)
                print(dept.no, dept.name, dept.location)
                result = cursor.fetchone()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
