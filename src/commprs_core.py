import re as __re

__COMMAND_NAME_EXTRAXTION_RGEX = r"(\(\"?).+(\"?\))"
__COMMAND_ARGS_SECTION_EXTRACTOR_REGEX = r"\(\"?.+\"?\)"  # the pattern \(\"?.+\"?\) gives us anything between two (), like sum(12) => the result will be 13

# [Just for Test] a dictionary of commands, it will be changed into anouther format
__comDict = {
    "sub": lambda args: int(args[0]) - int(args[1]),
    "sum": lambda args: int(args[0]) + int(args[1]),
    "mul": lambda args: int(args[0]) * int(args[1]),
    "dvd": lambda args: int(args[0]) / (args[1]),
    "hi": lambda args: "hi there, this is codeagha's simple command parser based on regex !"
    + (
        ("i've got your message : '" + " ".join(args) + "'")
        if (len(args) > 0)
        else ("")
    ),
    "exit": lambda args: exit(),
}


def __extractCommandName(mnCom):
    return __re.sub(__COMMAND_NAME_EXTRAXTION_RGEX, "", mnCom)  # to get the command name


def __extractCommandArguments(mnCom):
    outs = []
    args = __re.findall(__COMMAND_ARGS_SECTION_EXTRACTOR_REGEX, (mnCom))
    if len(args) == 0:
        return []
    for a in args[0].split(","):
        outs.append(a.replace("(", "").replace('"', "").replace(")", "").strip())
    return outs
    # to get the arguments section

def __splitComm(com):
    return __re.split(r"\;+\b", com)  # get the set of commands that inputed by user

def runCommand(_commName, _args):
    return __comDict[_commName](_args)

def runAll(com):
    _comSt = __splitComm(com)
    for _mnCom in _comSt:
        args = __extractCommandArguments(_mnCom.replace(" ", ""))
        commName = __extractCommandName(
            _mnCom
        )  # Call the command name extractor function
        yield runCommand(commName, args)

def runFirst(com):
    _comSt = __splitComm(com)
    _mnCom = _comSt[0] # only first run the command 
    args = __extractCommandArguments(_mnCom.replace(" ", ""))
    commName = __extractCommandName(_mnCom)  # Call the command name extractor function
    return runCommand(commName, args)
