from _datetime import datetime
import time
from mysqlHelper import MySqlHelper
from meta_class import Group, Book
import pymysql


class GroupController(object):
    def __init__(self, sql_helper):
        self._sql_helper = sql_helper

    def add_group(self, group):
        sql = "insert into t_group (g_title) values (%(title)s)"
        param = {
            'title': group.title
        }
        res = self._sql_helper.execute_dml(sql, param=param)
        if res > 0:
            return True
        else:
            return False

    def edit_group(self, group):
        sql = "update t_group set g_title=%(title)s where g_id=%(id)s"
        param = {
            'id': group.id,
            'title': group.title
        }
        res = self._sql_helper.execute_dml(sql, param=param)
        if res > 0:
            return True
        else:
            return False

    def delete_group(self, group):
        sql = "delete from t_group where g_id=%(id)s"
        param = {
            'id': group.id
        }
        res = self._sql_helper.execute_dml(sql, param=param)
        if res > 0:
            return True
        else:
            return False

    def query_all(self):
        sql = "select g_id,g_title from t_group"
        res = self._sql_helper.execute_dql(sql)
        group_list = []
        if res:
            for ele in res:
                # group = Group()
                # group.id = ele['g_id']
                # group.title = ele['g_title']
                group = Group(**ele)
                group_list.append(group)
        return group_list

    def query_one(self, *, id=None, title=None):
        if id:
            sql = "select g_id,g_title from t_group where g_id=%(id)s"
            param = {
                'id': id
            }
        elif title:
            sql = "select g_id,g_title from t_group where g_title=%(title)s"
            param = {
                'title': title
            }
        res = self._sql_helper.execute_dql(sql, param=param)
        if res:
            # group = Group()
            # group.id = res[0]['g_id']
            # group.title = res[0]['g_title']
            group = Group(**res[0])
            return group
        return None


class BookController(object):
    def __init__(self, sql_helper):
        self._sql_helper = sql_helper

    def add_book(self, book):
        sql = "insert into t_book (b_name,b_phone,b_address,b_gid,b_addtime) values " \
              "(%(name)s,%(phone)s,%(address)s,%(gid)s,%(addtime)s)"
        param = {
            'name': book.name,
            'phone': book.phone,
            'address': book.address,
            'gid': book.gid,
            'addtime': book.addtime,
        }
        res = self._sql_helper.execute_dml(sql, param=param)
        if res > 0:
            return True
        else:
            return False

    def edit_book(self, book):
        sql = "update t_book set b_name=%(name)s,b_phone=%(phone)s,b_address=%(address)s,b_gid=%(gid)s," \
              "b_addtime=%(addtime)s where b_id=%(id)s"
        param = {
            'id': book.id,
            'name': book.name,
            'phone': book.phone,
            'address': book.address,
            'gid': book.gid,
            'addtime': book.addtime
        }
        res = self._sql_helper.execute_dml(sql, param=param)
        if res > 0:
            return True
        else:
            return False

    def delete_book(self, book):
        sql = "delete from t_book where b_id=%(id)s"
        param = {
            'id': book.id
        }
        res = self._sql_helper.execute_dml(sql, param=param)
        if res > 0:
            return True
        else:
            return False

    def query_all(self):
        sql = "select b_id,b_name,b_phone,b_address,b_gid,b_addtime from t_book"
        res = self._sql_helper.execute_dql(sql)
        book_list = []
        if res:
            for ele in res:
                # book = Book()
                # book.id = ele['b_id']
                # book.name = ele['b_name']
                # book.phone = ele['b_phone']
                # book.address = ele['b_address']
                # book.gid = ele['b_gid']
                # book.addtime = ele['b_addtime']
                book = Book(**ele)
                book_list.append(book)
        return book_list

    def query_one(self, *, id=None, name=None):
        if id:
            sql = "select b_id,b_name,b_phone,b_address,b_gid,b_addtime from t_book where b_id=%(id)s"
            param = {
                'id': id
            }
        elif name:
            sql = "select b_id,b_name,b_phone,b_address,b_gid,b_addtime from t_book where b_name=%(name)s"
            param = {
                'name': name
            }
        res = self._sql_helper.execute_dql(sql, param=param)
        if res:
            # book = Book()
            # book.id = res[0]['b_id']
            # book.name = res[0]['b_name']
            # book.phone = res[0]['b_phone']
            # book.address = res[0]['b_address']
            # book.gid = res[0]['b_gid']
            # book.addtime = res[0]['b_addtime']
            book = Book(**res[0])
            return book
        return None


def main():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'root',
        'database': 'hrs',
        'port': 3306,
        'charset': 'utf8',
        'autocommit': False,
        'cursorclass': pymysql.cursors.DictCursor
    }
    sql_helper = MySqlHelper(config)
    group_c = GroupController(sql_helper)
    book_c = BookController(sql_helper)

    is_continue = True
    while is_continue:
        print('--------欢迎使用Alex私人通讯录系统--------')
        print('您可以使用的操作做如下：')
        print('新建组（按 1）')
        print('修改组（按 2）')
        print('删除组（按 3）')
        print('查看所有组（按 4）')
        print('-----------------------------------------')
        print('新建联系人（按 5）')
        print('修改联系人（按 6）')
        print('删除联系人（按 7）')
        print('查看所有联系人（按 8）')
        print('查看联系人信息（按 9）')
        print('-----------------------------------------')
        print('退出系统（按 0）')
        print()
        oper = input('请选择操作：')
        if oper == '0':
            is_continue = False
        elif oper == '1':
            title = input('请输入要创建的组名：')
            group = group_c.query_one(title=title)
            if not group:
                group = Group()
                group.title = title
                if group_c.add_group(group):
                    print('创建组成功...')
                else:
                    print('创建组失败，请重试...')
            else:
                print('已存在该组，请重试...')
        elif oper == '2':
            title = input('请输入要修改的组名：')
            group = group_c.query_one(title=title)
            if not group:
                print('不存在该组，请重试...')
            else:
                title = input('修改后的组名：')
                group.title = title
                if group_c.edit_group(group):
                    print('修改组成功...')
                else:
                    print('修改组失败，请重试...')
        elif oper == '3':
            title = input('请输入要删除的组名：')
            group = group_c.query_one(title=title)
            if not group:
                print('不存在该组，请重试...')
            else:
                if group_c.delete_group(group):
                    print('删除组成功...')
                else:
                    print('删除组失败，请重试...')
        elif oper == '4':
            group_list = group_c.query_all()
            print('%5s%10s' % ('组id', '组名'))
            for group in group_list:
                print('%5d%10s' % (group.id, group.title))
        elif oper == '5':
            g_title = input('请输入所属组：')
            name = input('请输入联系人姓名：')
            phone = input('请输入联系人电话：')
            address = input('请输入联系人地址：')
            group = group_c.query_one(title=g_title)
            if group:
                book = Book()
                book.name = name
                book.phone = phone
                book.address = address
                book.gid = group.id
                book.addtime = datetime.now()
                if book_c.add_book(book):
                    print('新建联系人成功...')
                else:
                    print('新建联系人失败，请重试...')
            else:
                print('不存在该组，请重试...')
        elif oper == '6':
            pass
        elif oper == '7':
            name = input('请输入要删除联系人的姓名：')
            book = book_c.query_one(name=name)
            if book:
                if book_c.delete_book(book):
                    print('删除联系人成功...')
                else:
                    print('删除联系人失败，请重试...')
            else:
                print('不存在该联系人，请重试...')
        elif oper == '8':
            book_list = book_c.query_all()
            print('%5s %10s %12s %10s %10s %12s' % ('id', '姓名', '电话', '地址', '所属组', '创建时间'))
            for book in book_list:
                print('%5s %10s %12s %10s %10s %12s' % (book.id, book.name, book.phone, book.address, book.gid, book.addtime))
        elif oper == '9':
            name = input('请输入要查询联系人的姓名：')
            book = book_c.query_one(name=name)
            if not book:
                print('不存在该联系人，请重试...')
            else:
                print('%d-%s-%s-%s-%s-%s' % (book.id, book.name, book.phone, book.address, book.gid, book.addtime))

        print()
        time.sleep(3)


if __name__ == '__main__':
    main()
