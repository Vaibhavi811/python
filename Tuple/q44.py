# count frequency of elements in a tuple
from collections import Counter
tuple= (2,2,2,56,67,56,89,4,4)

result= list(Counter(tuple).items())
print(result)
