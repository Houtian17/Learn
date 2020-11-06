from pymysql import connect


class Hero(object):
    def __init__(self):
        self.conn = connect(host='localhost', port=3306, user='root', database='python-01', charset='utf8')
        self.cursor = self.conn.cursor()

    def __delete__(self):
        self.cursor.close()
        self.conn.close()

    def excute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有的商品"""
        # 创建Connection 连接
        sql = "select * from heros"
        self.excute_sql(sql)

    @staticmethod
    def print_menu():
        print("--------hero--------")
        print("1：显示所有的英雄")
        return input("请输入对应的功能号：")

    def run(self):

        num = self.print_menu()
        if num == "1":
            self.show_all_items()
        else:
            print("输入有误，请重新11输入")


def main():
    hero = Hero()
    hero.run()


if __name__ == '__main__':
    main()
