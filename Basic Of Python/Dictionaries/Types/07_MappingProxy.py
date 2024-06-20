# types module, MappingProxyType creates a read-only view of a dictionary.

from types import MappingProxyType

writable_dict = {'a': 1, 'b': 2}
read_only_dict = MappingProxyType(writable_dict)

# read_only_dict['b'] = 3  # This will raise a TypeError
# writable_dict['c'] = 5  #Changes in bothe writable_dict and read_only_dict]

print(writable_dict)
print(read_only_dict)  # Output: {'a': 1, 'b': 2}

print(id(writable_dict))
print(id(read_only_dict))
