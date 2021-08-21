import numpy as np
import pandas as pd

while True:
    str = input()
    if len(str) < 8:
        res = str + '0' * (8 - len(str))
        print(res)
    else:
        time = len(str) // 8
        if len(str) % 8 == 0:
            for i in range(time):
                res = str[i*8: i*8 +8]
                print(res)
        else:
            for i in range(time):
                res = str[i*8: i*8 +8]
                print(res)
            print(str[time * 8:] + '0' * (8 - len(str[time * 8:])))





