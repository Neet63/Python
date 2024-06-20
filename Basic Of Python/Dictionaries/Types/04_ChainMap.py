# ChainMap groups multiple dictionaries into a single view.

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map)  
print(chain_map['b']) # Output will be 2 (from dict1, the first dictionary)
