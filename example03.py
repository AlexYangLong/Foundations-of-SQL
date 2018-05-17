import pymysql


def main():
    conn = pymysql.connect(
		'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'hrs',
        'port': 3306,
        'charset': 'utf8',
        'autocommit': False,
        'cursorclass': pymysql.cursors.DictCursor  # cursorclass设置cursor游标的类型)
		)
    try:
        with conn.cursor() as cursor:
            cursor.execute('select dno, dname, dloc from tbdept limit 3')
            result = cursor.fetchone()
            while result:
                print(result)
                print(result[1], result[2])
                result = cursor.fetchone()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
