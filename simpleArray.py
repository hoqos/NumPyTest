import numpy as np

a = np.arange(7)

print(a)
print(a[0])
print(a[-1])

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a[0,2])
b = a[1:]

print(b)
print(b % 3 == 0)
