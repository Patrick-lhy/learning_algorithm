import sys


class CheckPasswd:
    def __init__(self, passwd):
        self.passwd = passwd
        self.type_counter = 0
        self.check_str = False

    def check_type(self):
        type_set = set()
        for i in self.passwd:
            if i.isdigit():
                type_set.add(1)
            elif i.isalpha():
                if i.lower() == i:
                    type_set.add(2)
                else:
                    type_set.add(3)
            else:
                type_set.add(4)
        print(type_set)
        self.type_counter = len(type_set)

    def check_child(self):
        for i in range(len(self.passwd) - 3):
            if self.passwd.count(self.passwd[i:i + 3]) > 1:
                self.check_str = True
                break
            else:
                self.check_str = False

    def run_check(self):
        # 1.进行长度判断
        if len(self.passwd) <= 8:
            return 'NG'
        # 2.进行类型判断
        self.check_type()
        if self.type_counter < 3:
            return 'NG'
        # 3.字符串检查
        self.check_child()
        if self.check_str:
            return 'NG'
        return 'OK'


def main():
    while True:
        passwd = sys.stdin.readline().strip()
        if passwd == '':
            break
        result = CheckPasswd(passwd)
        print(result.run_check())


main()

