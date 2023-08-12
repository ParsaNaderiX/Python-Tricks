# Different ways to test multiple flags at once in Python

x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print("passed")

if 1 in (x, y, z):
    print("passed")


# these only test for truthiness :
if x or y or z:
    print("passed")

if any((x, y, z)):
    print("passed")


# All of different above ways work same .
