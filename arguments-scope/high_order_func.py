#Here you'll see the use of lambdas
from functools import reduce

#Map applies a function over all the elements in an iterable

values = [1, 2, 4, 9, 0, -9, 13]

print(f'Values: {values}')

mapped = map(lambda val: val*val, values)
print('Mapped values: ', list(mapped))

filtered = filter(lambda val: val<5, values)
print('Filtered values: ', list(filtered))

reduced = reduce(lambda item1, item2: item1 + item2, values)
print('Reduced value: ', reduced)