import pymysql

# 事务的特点是什么? - ACID特性
# 原子性(Atomicity): 不可分割要么全成功要么全失败
# 一致性(Consistency): 事务前后数据状态要保持一致
# 隔离性(Isolation): 多个事务不能看到彼此的中间状态(提交或回滚之前的状态)
# 持久性(Duration): 事务完成后数据要持久化(事务的影响要反映在物理存储上)


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
            dno = input('部门编号: ')
            # 这种写法有被SQL注射攻击(SQL Injection)的风险
            # sql = 'delete from dept where dno=%d' % dno
            # result = cursor.execute(sql)
            # 带占位符的SQL是没有被SQL注射攻击风险的推荐使用
            result = cursor.execute(
                'delete from dept where dno=%s',
                (dno, )
            )
            # 如果事务中的所有操作全部都成功了最后手动提交事务
            conn.commit()
            print('删除成功' if result == 1 else '删除失败')
    except:
        # 如果事务中的操作有任何一个发生了异常状况那么就回滚事务
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
