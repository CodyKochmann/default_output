# default_output
#### Overwrite the output of functions in python

#### Example Usage:

```python
# cleanly defines what comes out if something fails
@default_output(-1)
def count(i):
    """ returns the count of something """
    return len(i)

print("\n{}\n".format(count(5)))
```

#### Output

```
ERROR:root:object of type 'int' has no len()
Traceback (most recent call last):
  File "/tmp/scratch.py", line 18, in wrapper
    return f(*args, **kwargs)
  File "/tmp/scratch.py", line 34, in count
    return len(i)
TypeError: object of type 'int' has no len()

-1

```

The point of this is to be able to write functions and cleanly give them a backup output if something goes wrong within the function without hiding what actually went wrong.
