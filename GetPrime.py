def func():
    num = int(input())

    def getprime(n):
        i = 2
        while i*i <= n and n >= i:
            while n % i == 0:
                n = n//i
                print(i, end=' ')
            i = i + 1
        if n - 1:
            print(n, end=' ')
    getprime(num)


if __name__ == '__main__':
    func()

