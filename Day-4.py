# The get() method on dictionaries and its "default" argument

name_for_userid = {382: "Alice", 590: "Bob", 951: "Dilbert"}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(590))
# output is "Hi Bob!"
# because key=590 does exist in the dict and its value is 'Bob'

print(greeting(820))
# output is "Hi there!"
# because key=820 doesn't exist in the dict and default argument is 'there'


# When "get()" is called it checks if the given key exists in the dict.
# If it does exist, the value for that key is returned.
# If it does not exist then the value of the default argument is returned instead.
