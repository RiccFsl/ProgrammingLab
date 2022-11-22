def my_max(a,b):
    if a == b:
        print('i due numeri sono identici')
    elif a > b:
        print('il numero più grande tra i due è ' + str(a))
    else:
        print('il numero più grande tra i due è ' + str(b))

my_num1 = 1
my_num2 = 2
my_max(my_num1, my_num2)