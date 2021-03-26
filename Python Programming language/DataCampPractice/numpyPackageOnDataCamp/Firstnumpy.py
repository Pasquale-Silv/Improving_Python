"""
NumPy is a Python package to efficiently do data science.
Learn to work with the NumPy array,
a faster and more powerful alternative to the list,
and take your first steps in data exploration.
"""

import numpy

list1 = [1,2,3]
list2 = [1,2,3]

np_list1 = numpy.array(list1)
np_list2 = numpy.array(list2)

list3 = list1 + list2
print(list3)

np_list3 = np_list1 + np_list2
print(np_list3)
