def fun(num):

    if num[-1] != 0:
        temp = []
        num_list = list(num)
        for i in num_list[::-1]:
            if i not in temp:
                temp.append(i)
    else:
        print("该整数最后一位为0")

    string = "".join(temp)
    print(string)


fun(input())
