tuple_ = (1, 2, 'a', 'b')
print(tuple_)
# tuple_[1] = 6 . это вызовет ошибку,так как кортеж неизменяемый объект
# print(tuple_)
list_ = [1, 2, 'a', 'b', 'Modified']
print(list_)
list_[0] = 5
print(list_)
