# Lists
An ordered collection of "unnamed" variables. Instead of refering to the variables by name, we use their position

```python
xs = [1, 3, 5, 7] # create a list of x's

# output the value in the 1st position
print(xs[0]) # notice 0 = 1st position

# we can assign this value to another
# variable
x = xs[0]

xs[0] = 3 # we can also set this value

# the last value is the number of items
# minus 1
print(xs[3])

# so this will give you an error:
# because it goes past the number of items
print(xs[4])
```

## For-loops

In python, for-loops are built into collections.
We can write a for-loop like this:

```python
xs = [1, 2, 3]

for x in xs:
    print(x)

# 1
# 2
# 3

# we can get the index and value of the index
# together like this:
for i, x in enumerate(xs):
    print(i, x)
```