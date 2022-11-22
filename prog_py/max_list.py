def max_list(my_list):
    my_max = 0
    for num in my_list:
        if num > my_max:
            my_max = num
    print(f"il numero più grande della lista è {my_max}")
    print('il numero più grande della lista è {}'.format(my_max))


list = [1,2,3,4,5,6,7,8,9]
max_list(list)