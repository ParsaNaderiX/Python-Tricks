# How to sort a Python dictionary by value

# first way:
early_dict = {"a": 4, "b": 2, "c": 3, "d": 1}

sorted_dict = dict(sorted(early_dict.items(), key=lambda x: x[1]))

print("Result of first way: ", sorted_dict)
# output: Result of first way:  {'d': 1, 'b': 2, 'c': 3, 'a': 4}

# second way:
import operator

early_dict = {"a": 4, "b": 2, "c": 3, "d": 1}
sorted_dict = dict(sorted(early_dict.items(), key=operator.itemgetter(1)))

print("Result of second way: ", sorted_dict)
# output: Result of second way:  {'d': 1, 'b': 2, 'c': 3, 'a': 4}
