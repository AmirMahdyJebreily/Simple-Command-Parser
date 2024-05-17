# Simple Command Parser
a simple terminal command parser with a simple syntax in python based on regex  
-  
I started this project just for fun, but then I saw that it could be an interesting concept for a random repository on Github, especially that later a bigger idea came to my mind and I thought that the combination of this project and that idea could produce something interesting. As a result, I decided to develop it more!

## Using
Only clone the repo and import the `runAll` function from `commprs_core` module into your script : 
```bash
git clone https://github.com/AmirMahdyJebreily/Simple-Command-Parser.git
```
it have a very simple using method, take a look :  
```python
from commprs_core import runAll
com = input("Enter Command : ")
print(runAll(com))
```  
The `runAll` function will execute the commands defined in `_comDict` and you will see the output : 
```
Enter Command : sum(12,13)
25
```
