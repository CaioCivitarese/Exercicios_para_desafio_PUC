t = ('a', 'b', 'c', 'd', 'e')
t = ('A',) + t[1:]
t=(1,2,3,4)
print(t)

s = 'abc'
t = [0, 1, 2]
print(zip(s, t))
for pair in zip(s, t):
    print(pair)


d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)
for key, value in d.items():
    print(key, value)

directory=dict()
directory['sá', 'edu'] = 0
directory['silva', 'lala'] = 1
for last, first in directory:
    print(first, last, directory[last,first])
