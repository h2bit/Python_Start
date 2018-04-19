# 字符串处理函数
string = 'Python语言程序设计'

print(len(string), str(123456), hex(255), oct(8))
print(ord('A'), chr(65))
print('\n')

print(string.lower())
print(string.upper())
print(string.isupper())
print(string.islower())
print('\n')

print('123456'.isnumeric())
print('      '.isspace())
print(string.startswith('Python'))
print(string.endswith('语言程序设计'))
print(string.startswith('语言程序', 6, -2, ))
print('\n')

print('1,2,3'.split(','))
print('1,2,3'.split(',', 1))
print('11111'.replace('1', '2'))
print('11111'.replace('1', '2', 3))
print('Python语言程序设计'.center(40))
print('Python语言程序设计'.center(40, '-'))
print('\n')

print('111222333'.count('11'))
print('111222333'.count('11', 1))
print('111222333'.count('11', 3, -1))
print('12312312311'.strip('12'))
print('123'.zfill(10))
print('123'.zfill(2))
print('\n')



