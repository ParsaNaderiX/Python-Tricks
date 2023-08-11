# How to merge two dictionaries in Python 3.5+

x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}

z = {**x, **y}
print(z)

# output(z): {'a': 1, 'b': 3, 'c': 4}

w = {**y, **x}
print(w)

# output(w): {'b': 2, 'c': 4, 'a': 1}

"""
in above examples, Python merges dictionary keys in the order listed in the expression,
"overwriting duplicates from left to right".
pay attention about different values of 'b' (key) in two different merged dictionaries .
"""
