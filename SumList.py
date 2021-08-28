

def sum_list(numbers):
    n = len(numbers)
    if n == 0:
        return '该数组为空'
    if n == 1:
        return numbers[0]
    result = 0
    for i in range(n):
        right = n - 1
        while right > i:
            sum_num = sum(numbers[i:right+1])
            result = max(result, sum_num)
            right -= 1
    return result


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    r = sum_list(nums)
    print(r)


