from commprs_core import runAll

while True:
    com = input("Enter Command : ")
    res = runAll(com)
    for r in res:
        print(r)
