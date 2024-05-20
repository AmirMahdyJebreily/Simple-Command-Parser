# CodeAgha 2023
from src.commprs_core import runAll

print("Hi, Wellcome to CodeAgha Simple Command Parser")
print("Github repo:", "https://github.com/AmirMahdyJebreily/Simple-Command-Parser\n")
while True:
    commands = input("> ")  # get commands from imports
    results = runAll(
        commands
    )  # run all commands with "src.commprs_core" function runAll
    for res in results:  # iterate yield results
        if res != None:  # for filter printing noRes Functions
            print(":", res)  # print results ;)
