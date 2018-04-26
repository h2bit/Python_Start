import re

# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
# print("m.string:", m.string)
# print("m.re:", m.re)
# print("m.pos:", m.pos)
# print("m.endpos:", m.endpos)
# print("m.lastindex:", m.lastindex)
# print("m.lastgroup:", m.lastgroup, '\n')
#
# print("m.group(1,2):", m.group(1, 2))
# print("m.group(sign):", m.group('sign'))
# print("m.groups():", m.groups())
# print("m.groupdict():", m.groupdict())
# print("m.start(2):", m.start(2))
# print("m.end(2):", m.end(2))
# print("m.span(2):", m.span(2))
# print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))
#
# pattern = re.compile(r' ')
# list = pattern.split('dis 3 a:1 b:2 c')
# print(list)
# pname = list[0]
# num = int(list[1])
# for i in range(num):
#     name = list[i+2]
#     m = re.match(r'(?P<name>\w+):?(?P<number>\d+)?', name)
#     print(m, m.group('name'), m.group('number'))

# p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
# print("p.pattern:", p.pattern)
# print("p.flags:", p.flags)
# print("p.groups:", p.groups)
# print("p.groupindex:", p.groupindex)
#
# pattern = re.compile(r'world')
# match = pattern.search('hello world!')
# if match:
#     # 使用Match获得分组信息
#     print(match.group())
#
# p = re.compile(r'\d+')
# print(p.split('one1two2three3four4'))
#
# p = re.compile(r'\d+')
# print(p.findall('one1two2three3four4'))
#
# p = re.compile(r'\d+')
# for m in p.finditer('one1two2three3four4'):
#     print(m.group())

# p = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
# print(p.sub(r'\2 \1', s))
# print(p.subn(r'\2 \1', s))
#
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
#
# print(p.sub(func, s))
# print(p.subn(func, s))

# m = int(input())
# n = int(input())
# instrs = []
# value = []
# for i in range(m):
#     instrs.append(input())
# for i in range(m):
#     value.append(input())
f = open('input.txt', 'r')
readstr = f.readline().replace('\n', '')
m = int(readstr.split(' ')[0])
n = int(readstr.split(' ')[1])
# print(m, n)
instrs = []
dict = {}
pattern_input = re.compile(r'({{ (\w+) }})')
pattern_name = re.compile(r'(\w+) "(.+)"')
for i in range(m):
    instrs.append(f.readline().replace('\n', ''))
for i in range(n):
    match = pattern_name.match(f.readline().replace('\n', ''))
    if match is not None:
        dict[match.group(1)] = match.group(2)
        print(dict)
for i in range(m):
    searchh = pattern_input.search(instrs[i])
    while searchh is not None:
        # instrs[i] = pattern_input.sub(dict.get(searchh.group(1), ''), instrs[i])
        # searchh = pattern_input.search(instrs[i])
        instrs[i] = instrs[i].replace(searchh.group(1), dict.get(searchh.group(2), ''))
        searchh = pattern_input.search(instrs[i])
    else:
        print(instrs[i])