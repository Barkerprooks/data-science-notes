# Dicts (Dictionaries)
An unordered collection of variables. Instead of each variable having a name (like in `x = 23`, the name of the variable is `x`), each variable has a "slot" in the dictionary. each slot IS a value (like `1`, `99`, `"hello"`, `True`, etc...). So a dictionary is a mapping of two values. One is the "key" or index, or "slot". the other is the "value" that is being stored. You can think of the "key" value as the variable's name

```python
xs = {} # create an empty dict

config['theme'] = 'light'

xs["hello"] = "world" # we can create a new slot like this

x = xs["hello"] # then we can extract it later using the
                # same "key" value

if config["theme"] == "light":
    ... # do stuff to make a light theme
```

## Getting values from the dict
To get a value normally, we just "index" it like so
```python
x = xs["x"] # get the value with key x
```
One problem, what if the dict has no key `"x"`?
A: Runtime Error!!!!

If we want to safely get a value out with no errors,
we can. using the function `get`
```python
x = xs.get('x') # get the value with the key x
# What if x does not exist? then it will just be None
print(x) # output: None

# to change "default" value
x = xs.get('x', 'N/A')
print(x) # output: N/A
```

## For-loops

In python dictionaries, for-loops only loop through the keys
in the dict

```python

xs = {'a': 1, 'b': 2, 'c': 3}

for key in xs:
    print(key)
# a
# b
# c

for key, value in xs.items():
    print(key, value)

# a 1
# b 2
# c 3

# xs.values() works if you just want values
```
