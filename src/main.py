from commprs_core import runAll

while True:

    _com = input("Enter Command : ")
    _comSt = re.split(r"\;+\b", _com)  # get the set of commands that inputed by user

    print(runAll(_comSt))
