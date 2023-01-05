# text-file-api
This script is supposed to simplify the usage of a text file in python.  

## Overview
There are 4 functions available for use:
```
link(filename: str)
get(identifier: str)
post(identifier: str, resource: any)
delete(identifier: str)
```

## Usage
Import the module
```python
import crossfile
```
Instantiate the class
```python
cf = crossfile.Crossfile('database.txt')
```
Use the methods
```python
cf.post('a', 'foo')
cf.post('b', 'bar')
print(cf.get())
cf.delete('a')
print(cf.get())
```

## Example
[Example](example.py)
