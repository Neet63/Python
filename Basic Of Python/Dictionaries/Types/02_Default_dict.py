# Provided by the collections module, 
# defaultdict allows you to specify a default value for missing keys.

from collections import defaultdict

# Default value for int is 0
default_dict = defaultdict(int)
default_dict['count'] += 2
default_dict['count2'] += 2
print(default_dict)  # Output: defaultdict(<class 'int'>, {'count': 1})
