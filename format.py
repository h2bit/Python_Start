# string.format

print('{} qqwertyuiop {} asdfghjkl {}'.format(0, 1, 'string'))
print('{1} qqwertyuiop {2} asdfghjkl {0}'.format(0, 1, 'string'))
print('')

print("{0:30}".format('python'))
print("{0:>30}".format('python'))
print("{0:*>30}".format('python'))
print("{0:*^30}".format('python'))
# err print("{0:^*30}".format('python'))
print('')

print("{0:*^30}".format(123456))
print("{0:*^30,}".format(123456))
print("{0:.2f}".format(123.456))
print("{:*>30.2f}".format(123.456))
print("{0:.4}".format('python'))
# 填充 对齐 宽度 ,分隔 .精度 类型
print("{0:*>30,.2f}".format(1123.456))
print('')

print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(42))
print('{0:e},{0:E},{0:f},{0:%}'.format(321.123))

# e4.3TextProgress.py
import time

scale = 30
print("执行开始".center(scale // 2, '-'))
t = time.clock()
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, -t), end='')
    time.sleep(0.05)
print("\n" + "执行结束\n".center(scale // 2, '-'))

PM = 30
if 0<= PM < 35:
    print("空气优质，快去户外运动!")
elif 35 <= PM <75:
    print("空气良好，适度户外活动！")
else:
    print("空气污染，请小心！")