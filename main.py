from src.commprs_core import runAll

print("Hi, Wellcome to CodeAgha Simple Command Parser")
print("Github repo :", "https://github.com/AmirMahdyJebreily/Simple-Command-Parser\n")
while True:
    com = input("> ")
    res = runAll(com)
    for r in res:
        print(":", r)
