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
        'cursorclass': pymysql.cursors.DictCursor  # cursorclass设置cursor游标的类型
    }
    # Connection 创建连接
    conn = pymysql.connect(**config)  # **dict 可以将dict中的内容拆散成键值对

    try:
        # Cursor 创建游标 支持with上下文语法
        with conn.cursor() as cursor:
            # 发送SQL语句，execute() 返回受影响的行数
            res = cursor.execute('insert into TbDept values (%(no)s, %(name)s, %(loc)s)',
                                 {'no': 1122, 'name': 'qwedfv', 'loc': 'sdf'})
            print(res)
            res = cursor.execute('select dno, dname, dloc from TbDept')
            print(res)
            res = cursor.fetchone()
            while res:
                print(res)
                dept = Dept(**res)
                print(dept.dname)
                res = cursor.fetchone()

            # 手动提交
            conn.commit()
    except BaseException as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
