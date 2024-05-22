# Simple Command Parser
a simple terminal command parser with a simple syntax in python based on regex  
-  
I started this project just for fun, but then I saw that it could be an interesting concept for a random repository on Github, especially that later a bigger idea came to my mind and I thought that the combination of this project and that idea could produce something interesting. As a result, I decided to develop it more!

## Using
Only clone the repo and import the `runAll` function from `commprs_core` module into your script : 
```bash
git clone https://github.com/AmirMahdyJebreily/Simple-Command-Parser.git
```  
## Python API
To complete the execution of the commands, you need to get the result of the command execution and print it anywhere you want. In this example, we use Python's own `print()`.
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
You should use the function `runAll` which yields the results, as you can see in [`main.py`](https://github.com/AmirMahdyJebreily/Simple-Command-Parser/blob/main/main.py) you will also need a loop:  
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
### Define your commands
For this case, you have to import `defCommand()` function. As you can see in [`main.py`](https://github.com/AmirMahdyJebreily/Simple-Command-Parser/blob/main/main.py) this function gets a __string name__ and a handler function :
```python
from src.commprs_core import defCommand

def SumIntCollection(nums : list) -> int: # handler function
    res = 0
    for n in nums:
        res += int(n)
    return res

defCommand("sumAll", SumIntCollection)
```  
Its usefull when you want to test manual your script functions and give diffrent argument to there. now you can run the command like below : 
```
> sumAll(1, 2, 3)
: 6
> sumAll(sum(1,2), 3, 3)
: 9
```
Note that the arguments that are passed are all strings
## Syntax
### Define variables
Pay attention, this is not a programming language, so it can be said that these are exactly the variables of programming languages, but it can be said that the software actually gives names to different data and stores them in its memory so that they can be retrieved later, for this reason, I decided to name them Variable so that the names are not complicated and useless.  
There are two ways to define these variables
#### The first way to define variables
You can use the `var()` command. the `var()` is a default command that define a variable  
```
> var(x, 12)
```  
Now if you enter the name of the variable, the Command Parser will show you the value of the variable  
```
> x
: 12
```
#### The second way to define variables
The second method does the same work as the first method and has no difference in implementation, this method is provided only for convenience in defining the variables! You can use `$` operator to define variables!  
```
> $x = 12
```  
As before, if you enter the name of the variable, you will see their value  
```
> x
: 12
```
Pay attention, currently it is not possible to define a variable without an initial value, because these are not variables at all. In fact, you will need these when you want to store values in temporary memory to retrieve them later. Well, when there is no value, you won't need to save and restore it again :)  

## A slightly complicated example
So far, not many complex capabilities have been added to the syntax, but complex commands can also be written that show what complexities this project based on Rex can analyze.  
```
> $x = sum(1,mul(12,2))
> $y = 13
> sum(x, y)
: 38
```
It is not a very complicated thing for compilers of programming languages, but as a Command Parser it is a bit more complicated, especially that in the future facilities will be provided and these commands `sum` and `mul` etc. will be removed so that you can write commands yourself.  Inject yourself based on personalized regexes and have your own command system!  
 
I will be happy to support this project.  For now it's just a simple start, for another personal project, but I think it will be useful to some people!
