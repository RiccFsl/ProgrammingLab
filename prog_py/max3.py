def max_3(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= c and b >= a):
        return b
    else:
        return c


x = 1
y = 2
z = 3
max_3(x,y,z)