def sum(a):
    if a == 0:
        return
    else:
        print(a, "is request sum(a)")
        a -= 1  # a = a -1
        sum(a)


sum(8)
