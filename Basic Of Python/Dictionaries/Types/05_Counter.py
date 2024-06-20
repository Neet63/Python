# Counter is a special dictionary for counting hashable objects.

from collections import Counter

counter = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(counter)  # Output: Counter({'a': 3, 'b': 2, 'c': 1})
