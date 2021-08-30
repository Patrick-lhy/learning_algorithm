def shell_sort(numbers):
    """
    希尔排序
    :param numbers:
    :return:
    """
    n = len(numbers)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if numbers[i] < numbers[i - gap]:
                    numbers[i], numbers[i - gap] = numbers[i - gap], numbers[i]
                    i -= gap
                else:
                    break
        gap //= 2

    print(numbers)


if __name__ == '__main__':
    data = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
    shell_sort(data)
