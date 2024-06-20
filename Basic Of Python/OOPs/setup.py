#to use mypackage folder's module any where in system with help of pip 
# We have to set it up by follow:

from setuptools import setup
setup(name='mypackage',
version='0.1',
description='Package setup script',
url='#',
author='anonymous',
author_email='test@gmail.com',
license='MIT',
packages=['mypackage'],
zip_safe=False)