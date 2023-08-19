# How to remove duplicates from an ordered list :

# first way:
# Using Set:
# the fastest way is to convert to a set and back to a list:
duplicates = [1, 2, 1, 5, 7, 9, 3, 5, 2, 7, 10]
uniqe = list(set(duplicates))

print(uniqe)
# output is: [1, 2, 3, 5, 7, 9, 10]
# but this does not retain the item order (it will be sorted).


# second way:
# Using Dictionary:
# a set is a special case of a dict with only keys and no value.
d = {
    1: None,
    2: None,
    1: None,
    5: None,
    7: None,
    9: None,
    3: None,
    5: None,
    2: None,
    7: None,
    10: None,
}

print(list(d))
# output is: [1, 2, 5, 7, 9, 3, 10]
# dict preserves insertion order.


# third way:
# we can use dict.fromkeys() to make a list into a dict with None values:
items = [1, 2, 1, 5, 7, 9, 3, 5, 2, 7, 10]

print(list(dict.fromkeys(items)))
# output is: [1, 2, 5, 7, 9, 3, 10]
# dict preserves insertion order.
