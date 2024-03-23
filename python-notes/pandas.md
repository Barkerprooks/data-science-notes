# The Pandas Library

To use the library, we import it like
any other
```python
import pandas
```

You might see it like this in some tutorials
```python
import pandas as pd
```

## Ways to look at data
#### Mean
In statistics we have an idea called the "mean"
of the data set. We might want to know more about the data than we can tell from any single point, or record of data, so we can use things like the "mean" to help us better understand the collection of samples we have.
```python
import pandas as pd

df = pd.DataFrame([1, 2, 3])
print(df.mean()) # gives us: 2.0
```

#### Median
The median, like the average (mean), helps us to describe the middle of our data set. The median is the number that is spacially, or positionally, in the middle. When there is
an even number of items (no exact middle)
then we calculate the average of those two
values

- ex 1: [1, 2, 3, 4, 5] <- 3 is the median
- ex 2: [1, 2, 3, 4]

```python
import pandas as pd

df = pd.DataFrame([1, 2, 3, 4])
print(df.median()) # gives us: 
```