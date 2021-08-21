import sys


class PasswdEncoder:
    def __init__(self, passwd):
        self.passwd = passwd
        self.enc_passwd = ''
        self.alpha_2_num = {'abc': 2, 'def': 3, 'ghi': 4, 'jkl': 5, 'mno': 6, 'pqrs': 7, 'tuv': 8, 'wxyz': 9}

    def enc_process(self):
        for i in self.passwd:
            if i.isalpha():
                if i.lower() == i:
                    for sub_key in self.alpha_2_num:
                        if i in sub_key:
                            self.enc_passwd += str(self.alpha_2_num[sub_key])
                            break
                else:
                    if i == 'Z':
                        self.enc_passwd += 'a'
                    else:
                        self.enc_passwd += chr(ord(i.lower()) + 1)
            else:
                self.enc_passwd += i


def main():
    while True:
        passwd = sys.stdin.readline().strip()
        if passwd == '':
            break

        passwd_enc = PasswdEncoder(passwd)
        passwd_enc.enc_process()
        print(passwd_enc.enc_passwd)


main()