stu = {
    "name": "santhosh",
    "id": 2025,
    "course": "python"
}
#get() method is used to retrieve the value of a key from the dictionary. If the key is not found, it returns a default value (which can be specified as the second argument). If the second argument is not provided, it returns None.
print(stu.get("name"))
print(stu.get("id", "id not found"))
#keys() method returns a view object that displays a list of all the keys in the dictionary.
print(stu.keys())
#values() method returns a view object that displays a list of all the values in the dictionary.
print(stu.values())
#items() method returns a view object that displays a list of all the key-value pairs in the dictionary.
print(stu.items())
#pop() method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError. You can also provide a default value as the second argument to avoid the error.
print(stu.pop("course"))
print(stu)
#popitem() method removes and returns an arbitrary key-value pair from the dictionary. If the dictionary is empty, it raises a KeyError.
print(stu.popitem())
print(stu)
#setdefault() method returns the value of the specified key. If the key does not exist, it inserts the key with the specified value and returns that value. If the key already exists, it returns the existing value without modifying the dictionary.
print(stu.setdefault("course", "python"))
print(stu)
#keysfromkeys() method is a class method that creates a new dictionary with the specified keys and a default value. The keys are provided as an iterable (like a list or set), and the default value is assigned to all keys in the new dictionary.
d = dict.fromkeys(stu, 0)
print(d)
