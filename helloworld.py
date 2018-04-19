print("Hello World!")

import os
from datetime import datetime

now = datetime.now()

'''
多行注释
'''

print(now)
print(now.strftime("%X"))  # 单行注释
print(now.strftime("%x"))

print('单引号"双引号"')
print("双引号'单引号'")
print('''三个单引号
"双引号'单引号'"
'单引号'
换行
''')
print('python\t程序\t设计')

str = '123456'
print(str)
print(str[0:])
print(str[0:-1])
str = 'Python语言程序设计'
print(str[0], str[6])
print(str[: 6])
print(str[6: ])


if '1' in str:
    print('find 1')
elif '2' in str:
    print('find 2')
else:
    print('not find')

print(range(1, 10))
print(list(range(1, 10)))


def print_str(valstr):
    print('转化数字={:.2f}'.format(eval(valstr) / 3 - 50))


str = '250'
print_str(str)


def calc(a, b):
    print('sum', a + b)
    print('sub', a - b)
    print('cheng', a * b)
    print('divide', a / b)
    print('mod', a % b)
    print('shang', a // b)
    print('pow', a ** b)


calc(10, 3)

import  math
print(math.factorial(4))
print(math.gamma(1/2))

