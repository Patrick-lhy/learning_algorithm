

def Select_Sort(numbers):
    size = len(numbers)
    # 定义一个指针

    for i in range(size):
        k = i
        j = size - 1
        while i < j:
            if numbers[j] < numbers[k]:
                k = j
            j -= 1
        temp = numbers[i]
        numbers[i] = numbers[k]
        numbers[k] = temp

    print(numbers)


if __name__ == '__main__':
    data = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    Select_Sort(data)


