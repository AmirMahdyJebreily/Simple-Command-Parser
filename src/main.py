from commprs_core import runAll

while True:
    com = input("> ")
    res = runAll(com)
    for r in res:
        print(r)
