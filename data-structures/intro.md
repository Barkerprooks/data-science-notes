# Data Structures
Three basic data structures or "containers" in python:
- List
- Tuple
- Set
- Dictionary

### Lists
Ordered set of values. they stay in the same order that you put them in

A list with no values is called an "empty list"

You can make an empty list like this:
```python
my_list = [] # nothing inside
my_list = list() # this also works
```

We can add values into our list like this!
```python
my_list.append(1)
my_list.append(7)
```

And now this is what it looks like:
```python
print(my_list) # outputs: [1, 7]
```

Lets say we have a specific value we want to remove. We can search for, and delete the first occurance found like this:
```python
my_list.remove(1)
print(my_list) # outputs: [7]
```

We can access values directly in the list by their position. The positions start from 0, and go until the length of the list - 1. If we try to get anything outside of these boundaries, we get an `IndexError`:

```python
# lets make a new list
my_list_v2 = [1, 2, 3, 4]
# get the first item
item1 = my_list_v2[0]
# get the last item
item4 = my_list_v2[3]

print(item1, item4) # outputs: 1 4

# now lets set new values in the list
my_list_v2[0] = 4
# set the second item to 7
my_list_v2[1] = 7

print(my_list_v2) # outputs: [4, 7, 3, 4]
```

### Tuple
Tuples are very simple. You can think of a tuple like a list, only you cannot change the contents of a tuple

Make an empty tuple:
```python
my_tuple = ()
my_tuple = tuple()
```

Lets see what happens when we try to set items in the tuple
```python
# lets make a tuple
my_tuple = (1, 2, 3, 4)
# get the first item
item1 = my_tuple[0]
# get the last item
item4 = my_tuple[3]

print(item1, item4) # outputs: 1 4

# now lets set new values in the set
my_tuple[0] = 4 # ERROR: cannot set items in a set

print(my_tuple) # outputs: (1, 2, 3, 4)
```

### Sets
Sets are _UNIQUE_ collections. You cannot put more than _ONE_ of the same value in a set. Sets can give us a significant speedup in some cases

Create an empty set:
```python
my_set = set()
```

We can also create a set with items already in it like this:
```python
my_set = {1, 2, 3}
```

If we add more than one of the same value, it is ignored:
```python
my_set = {1, 2, 3, 3}
print(my_set) # outputs: {1, 2, 3}
```

We can add items to a set like so:
```python
my_set.add(4) # this is added
my_set.add(4) # this is not added
```

We can delete items the same way we would with a list:
```python
my_set.remove(2)
print(my_set) # outputs: {1, 3, 4}
```

### Dictionaries or Dicts

A Dictionary is like a set, only we are in control over where the value goes when we put it in the container. That way, we can reference the same position later and get the same thing back!

```python
my_dict = {}
my_dict = dict()
```

Lets add an item to our empty dict:
```python
my_dict['key'] = 1 # this adds the value 1 at the key 'key'
```

Now lets access it:
```python
value = my_dict['key']
print(value) # outputs: 1
```

What happens if we try to access something that isn't there? We will get a `KeyError`:
```python
value = my_dict['i dont exist']
# ERROR: KeyError
```

We can make a dictionary with pre-filled values like this:
```python
my_dict = {
    'player': {
        'health': 100,
        'level': 1
    },
    'settings': {
        'graphics': 'high',
        'fov': 120
    }
}
```

What if we want to delete settings?
```python
del my_dict["settings"]
```

A special feature of dicts is that we can look things up _REALLY_ fast. Imagine you have a list with 1,000,000,000,000,000,000 items in it. Thats a lot, even for your computer. It will need to check each and every index for the value. this will take _FOREVER_. If we use a set, the lookup is instant