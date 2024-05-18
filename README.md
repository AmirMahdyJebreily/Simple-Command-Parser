# Simple Command Parser
a simple terminal command parser with a simple syntax in python based on regex  
-  
I started this project just for fun, but then I saw that it could be an interesting concept for a random repository on Github, especially that later a bigger idea came to my mind and I thought that the combination of this project and that idea could produce something interesting. As a result, I decided to develop it more!

## Using
Only clone the repo and import the `runAll` function from `commprs_core` module into your script : 
```bash
git clone https://github.com/AmirMahdyJebreily/Simple-Command-Parser.git
```
### Execute only one command
it have a very simple using method, take a look :  
```python
from commprs_core import runFirst
com = input("Enter Command : ")
print(runFirst(com))
```  
The `runFirst` function will execute the commands defined in `_comDict` and you will see the output : 
```
> sum(12,13)
: 25
```
### Run multiple commands
You should use the function `runAll` which yields the results, as you can see in [`main.py`](https://github.com/AmirMahdyJebreily/Simple-Command-Parser/blob/main/src/main.py) you will also need a loop:  
```python
from commprs_core import runAll
com = input("Enter Commands : ")
res = runAll(com)
for r in res:
  print(r)
```
The `runAll` function will execute the commands defined in `_comDict` and you will see the output : 
```
> sum(12,13);mul(1,2)
: 25
: 2
```  
thanks for reading...
