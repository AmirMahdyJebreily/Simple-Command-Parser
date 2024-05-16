import re


_COMMAND_NAME_EXTRAXTION_RGEX = r"(\(\"?).+(\"?\))"
_COMMAND_ARGS_SECTION_EXTRACTOR_REGEX = r"\(\"?.+\"?\)" # the pattern \(\"?.+\"?\) gives us anything between two (), like sum(12) => the result will be 13

_comDict = {
        "sub": lambda args : args[0] - args[1],
        "sum": lambda args : args[0] + args[1],
        "mul": lambda args : args[0] * args[1],
        "dvd": lambda args : args[0] / args[1],
        "exit": lambda args : exit,
}

def extractCommandName(mnCom):
    return re.sub(_COMMAND_NAME_EXTRAXTION_RGEX, '', mnCom) # to get the command name

def extractCommandArguments(mnCom):
    outs = []
    for a in re.findall(_COMMAND_ARGS_SECTION_EXTRACTOR_REGEX, (mnCom))[0].split(","):
        outs.append(int(a.replace("(","")
                        .replace("\"","")
                        .replace(")","")
                        .strip()))
    return outs
    # to get the arguments section

def runCommand(_commName, _args): 
    return _comDict[_commName](_args)

while True :
    
    _com = input("Enter Command : ")
    _comSt = re.split(r"\;+\b", _com) # get the set of commands that inputed by user

    for _mnCom in _comSt :
        args = extractCommandArguments(_mnCom.replace(" ", ""))
        commName = extractCommandName(_mnCom) # Call the command name extractor function
        print(runCommand(commName, args))
