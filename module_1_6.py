my_dict = {'Masha': 1998, 'Danil': 2004, 'Anna': 1979}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Dasha'))
my_dict.update({'Diana': 2005, 'Anton': 1988})
print(my_dict)
a = my_dict.pop('Masha')
print(a)
print(my_dict)
my_set = {2, 2, 8, 'Dana' , 'Vova', 'Dana', 3.1, 3.2, 3.3, 3.1}
print(my_set)
my_set = {2, 2, 8, 'Dana' , 'Vova', 'Dana', 3.1, 3.2, 3.3, 3.1, 'pepefrog', 123}
print(my_set.discard('Dana'))
print(my_set)


