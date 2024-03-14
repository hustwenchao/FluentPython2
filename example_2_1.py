from collections import abc

print(issubclass(tuple, abc.Sequence))
print(issubclass(list, abc.MutableSequence))

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# shorter version
codes = [ord(symbol) for symbol in symbols]
print(codes)

# using list comprehension
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# another method using filter and map
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# Cartesian product using list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)
