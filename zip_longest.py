from itertools import zip_longest
name = ['surya', 'dk', 'saran', 'mahi', 'vikash', 'jayashri']
salary = [1000, 1234, 2345, 4532]
d = {}
for i, j in zip_longest(name, salary, fillvalue=0):
    key = i
    value = j+j*5//100
    d[key] = value
print(d)
