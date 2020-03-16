# text-file-api
This script is supposed to simplify the usage of a text file in python.  

## Overview
There are 4 functions which you can use to your advantage to make reading and writing to text files easy.  
This script includes the functions:
- `link()`
- `get()`
- `post()`
- `delete()`

## Setup  
1. To get started, import the script into you own script as a module.  
It doesn't matter wether you put this script into the python site packages folder, or in the same directory as your own code.  
Use `import crossfile` to import the script.

2. After importing the script, you must make an instance of the class so that python doesn't throw any errors.  
For example, `a = crossfile.api()` will create an instance of the `api()` class called `a`.

## Usage
- The `link()` function takes one parameter, which is the string name of the text file to be accessed.  
When used, it will return `'linked to: ' + self.dataname`, indicating that the script can communicate with the chosen file.  
This function can be used again to change which text file is being accessed by the script, allowing you to access multiple text files with the same instance.

- The `get()` function again, takes one parameter, which is an identifier (this is unique to each resource in the text file).  
When used, the function will search the text file for the resource with the given identifier.  
For example, if a resource has the indentifier `'hello'`, then you can use `a.get('hello')` to get the data from that resource.  
The `get()` function can also retrieve all of the data stored in the text file, by passing `''` as the parameter.

- The `post()` function takes 2 parameters, an identifier and some string data.  
It then adds to the text file a line which contains the identifier at the start, followed by a comma and then the string data.  
For example, doing `a.post(78,'blueberry')` will put `78,blueberry` into the text file.

- The `delete()` function takes one parameter, an identifier.  
It will then search the text file and remove the line which contains the given identifier.  
For example, `a.delete(78)` will remove the resource `78,blueberry` from the text file.

## Example
Here is an example of how you could use this script: [Example](example.py)
