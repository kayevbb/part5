# part5


import re

q = int(input())

for _ in range(q):
    a = input()
    b = input()
    
    regexp = '^[a-z]*%s[a-z]*$' % '[a-z]*'.join('[%s%s]' % (letter, letter.lower()) for letter in b)
    
    if re.search(regexp, a):
        print('YES')
    else:
        print('NO')
