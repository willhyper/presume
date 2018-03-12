# presume
decorator handling exception.

```python
from presume import presume, then

@presume(KeyboardInterrupt, action=then.save, args=('temp', var))
def main():
    ....
	
```
when an ```exception``` is raised, ```action``` is invoked.

The example here is when ```KeyboardInterrupt``` is raised, ```then.save('temp', var)``` is invoked.

```then.save``` is to pickle ```var``` and write it to the 'temp' file.

```@presume``` is chain-able:


```python
from presume import presume, then

@presume(KeyboardInterrupt, action=print, args=('load var by pickle.load',))
@presume(KeyboardInterrupt, action=then.save, args=('temp', var))
def main():
    ....
	
```
