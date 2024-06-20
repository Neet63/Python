# UserDict is a wrapper around dictionary objects for easier subclassing.
# allows you to create your own dictionary-like objects by inheriting from UserDict

from collections import UserDict

class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)

my_dict = MyDict()
my_dict['a'] = 10  
my_dict['b'] = 20
print(my_dict)  # Output: {'a': 10}
