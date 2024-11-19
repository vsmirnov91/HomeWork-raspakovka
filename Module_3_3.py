def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1)
print_params(2, 2, 2)
print_params(b = 25) #работает
print_params(c = [1,2,3]) #работает

values_list = [1, 'строчечка', False]
values_dict = {'a':1, 'b':'котики', 'c':False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [25, 'собачки']
print_params(*values_list_2, 42) #так же работает