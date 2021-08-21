while True:
    try:
        s, a = input(), {}
        for i in s:
            a[i] = s.count(i)
        b = sorted(a.values())
        print(b)

        for key, value in a.items():
            if b[0] == value:
                s = s.replace(key, "")
        print(s)
    except:
        break