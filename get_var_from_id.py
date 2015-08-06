import ctypes
a = "hello world"
print id(a)
print ctypes.cast(id(a), ctypes.py_object).value


var = 'I need to be accessed by id!'
address = id(var)
print(address)
var2 = [x for x in globals().values() if id(x)==address]
