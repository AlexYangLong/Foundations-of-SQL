import pymysql


def main():
    # 创建Connection对象
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
        # 创建Cursor对象
        # Cursor对象支持上下文语法可以放在with中
        with conn.cursor() as cursor:
            # 向数据库发出SQL语句
            # execute方法返回受影响的行数
            dno = int(input('部门编号: '))
            dname = input('部门名称: ')
            dloc = input('部门所在地: ')
            # 如果使用字符串格式化的方式来组装SQL语句
            # 最大的风险是用被SQL注射(SQL Injection)攻击的风险
            """
            sql = 'insert into tbdept values (%d, "%s", "%s")' % \
                  (dno, dname, dloc)
            print(sql)
            result = cursor.execute(sql)
            """
            # 写带占位符的SQL语句是我们推荐使用的方式
            result = cursor.execute(
                'insert into tbdept values (%(no)s, %(name)s, %(loc)s)',
                {'no': dno, 'name': dname, 'loc': dloc}
            )
            print(result)
            # 手动提交之前的操作
            conn.commit()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
