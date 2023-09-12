import unittest.mock as mock

# create a Mock
m = mock.Mock()
print("Print the type of Mock object")
print(type(m))

# mocks any attribute as a Mock
print("Mocking 'some_attribute'.. print attribute and its type")
print(m.some_attribute)
print(type(m.some_attribute))

# mock a method with user defined behaviour
print("Mocking 'some_method's return value")
m.some_method.return_value = "abc"
print(m.some_method())
