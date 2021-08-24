def convert(s: str, numRows: int) -> str:
    if numRows == 1:  # 如果指定行数为1行则直接返回字符串
        return s
    rows = {}  # 建立行和字符的映射
    index = 0  # 通过index遍历字符串
    i = 1  # 行号
    up = False  # 标记当前的字符位置是向上放还是向下
    while index < len(s):  # 遍历字符串
        rows[i] = rows.get(i, '') + s[index]  # 将字符添加到对应行
        index += 1  # 字符串索引+1

        if i == numRows:  # 如果是行号为指定行号说明触底，此时字符应该向上走
            up = True
        elif i == 1:  # 如果行号为1，则说明触顶，此时字符应该向下走
            up = False

        if up:  # 根据UP标记更新行号
            i -= 1
        else:
            i += 1
    temp = ''
    for j in range(1, numRows + 1):  # 从字典中根据行号取出字符串
        temp = temp + rows.get(j, '')

    return temp


if __name__ == '__main__':
    print(convert(s="PAYPALISHIRING", numRows=3))
