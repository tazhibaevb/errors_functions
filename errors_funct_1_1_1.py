# 1.1.1 Дан словарь в котором ключи должны быть только строковыми объектами,
# но может встретиться Int, как в качестве ключа, но ваша проверка только проверяет на строку
# и поэтому у вас выходит баг, ваша задача обработать исключением ошибку TypeError

# try:
#     dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}
#     for x in dict_.keys():
#         x + 'abc'
#         print(type(x),x)
# except TypeError:
#     x = str(x)
#     x + 'abc'
# print(type(x), x)
