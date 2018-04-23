File = open("test.txt", 'r')
text = File.readline()
print(text, end='')
File.seek(0)
for line in File:
    print(line, end='')
print('')
File.close();

import json

diction = {'a': 1, 'b': 2, 'c': 3}
s1 = json.dumps(diction)
print(s1)
s2 = json.dumps(diction, sort_keys=True, indent=4)
print(s2)
