import pymysql


def main():
    # Connection 创建连接
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           database='hrs',
                           port=3306,
                           charset='utf8',
                           autocommit=False)

    try:
        # Cursor 创建游标 支持with上下文语法
        with conn.cursor() as cursor:
            # 发送SQL语句，execute() 返回受影响的行数
            # res = cursor.execute('insert into TbDept values (%s, %s, %s)', (52, "总经办2", "北京2"))
            # print(res)
            res = cursor.execute('delete from TbDept where dno=%s', (51, ))
            print(res)
            # res = cursor.execute('select * from TbDept')
            # print(res)

            # 手动提交
            conn.commit()
    except BaseException as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()



if __name__ == '__main__':
    main()
