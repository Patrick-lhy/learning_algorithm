

def insert_sort(numbers):
    size = len(numbers)

    for i in range(size):
        j = i
        temp = numbers[i]
        while j > 0 and temp < numbers[j-1]:
            numbers[j] = numbers[j-1]
            j -= 1
        numbers[j] = temp
        print(numbers)


if __name__ == '__main__':
    data = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    insert_sort(data)


