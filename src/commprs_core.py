import re as __re
import src.commprs_tool as tool
import os

__VAR_DETECTION = r"\$\w+\s*\<{0,1}\=\s*.+"
__COMMAND_NAME_EXTRAXTION_RGEX = r"(\(\"?).+(\"?\))"
__COMMAND_ARGS_SECTION_EXTRACTOR_REGEX = r"\(\"?.+\"?\)"  # the pattern \(\"?.+\"?\) gives us anything between two (), like sum(12) => the result will be 13

# dictionary of variables
__varsDict = {
    "!version": "0.0.1",  # default variable
}

# [Just for Test] a dictionary of commands, it will be changed into anouther format
__comDict = {
    "sub": lambda args: int(args[0]) - int(args[1]),
    "sum": lambda args: int(args[0]) + int(args[1]),
    "mul": lambda args: int(args[0]) * int(args[1]),
    "dvd": lambda args: int(args[0]) / int(args[1]),
    # syntax commands :
    "var": lambda args: __defVariable(args[0], args[1]),
    # default commands :
    "hi": lambda args: "hi there, this is codeagha's simple command parser based on regex !"
    + (
        ("i've got your message : '" + " ".join(args) + "'")
        if (len(args) > 0)
        else ("")
    ),
    "exit": lambda args: exit(),
    "clear": lambda args: tool.runNoRes(
        os.system, "cls" if os.name == "nt" else "clear"
    ),
    # default for fun commands :
    "!mkemptscrn": lambda args: chr(27) + "[2J" + " ".join(args),
    "!pishi": lambda args: "meow ;) " + " ".join(args),  # for my friend, pishi :)
}


def __defVariable(varname: str, value):  # defind variable
    if __re.fullmatch(r"[a-z]+\w*", varname):
        __varsDict[varname] = value
    else:
        print(": [SyntaxError]: Var name is unvalid", varname)  # error handeling


def __extVariable(varname: str):
    if (varname) in __varsDict.keys():
        return __varsDict[varname]  # value if the variable
    else:
        print(
            ": [IdentifyError]: i do not identify var or function as name", varname
        )  # error handeling

def __checkVarName(varname: str):
    return varname in __varsDict.keys()

def __extractCommandName(mnCom):
    return __re.sub(
        __COMMAND_NAME_EXTRAXTION_RGEX, "", mnCom
    )  # to get the command name


def __extractCommandArguments(mnCom):
    outs = []
    args = __re.findall(__COMMAND_ARGS_SECTION_EXTRACTOR_REGEX, (mnCom))
    if len(args) == 0:
        return []
    
    for a in args[0].split(","):
        arg = a.replace("(", "").replace('"', "").replace(")", "").strip()
        if(__checkVarName(arg)):
            arg = __extVariable(arg)
        outs.append(arg)
    return outs
    # to get the arguments section


# spliter functions
def __splitComm(com):
    return __re.split(
        r"\s*\;+\s*\b", com
    )  # get the set of commands that inputed by user


def __splitDefVarComm(com):
    return __re.split(r"\s*\=+\s*\b", com)


# command identifier functions
def __isVarExtComm(com) -> bool:
    return (com) in __varsDict.keys() and ((com) not in __comDict.keys())


def __isVarDefAsignComm(com) -> bool:
    return __re.match(__VAR_DETECTION, com)


# runner functions
def runCommand(_commName, _args):
    return __comDict[_commName](_args)


def runFirst(_mnCom):
    args = __extractCommandArguments(_mnCom.replace(" ", ""))
    commName = __extractCommandName(_mnCom)  # Call the command name extractor function

    if __isVarExtComm(commName):
        return __extVariable(commName)  # variable extraction
    
    elif __isVarDefAsignComm(commName):
        parts = __splitDefVarComm(commName)
        return __defVariable(parts[0].replace(" ", "").replace("$", ""), parts[1])

    # if command isn't var of defVar or etc..., comman runner try to run it
    return runCommand(commName, args)


def runAll(com):
    _comSt = __splitComm(com)
    for _mnCom in _comSt:
        yield runFirst(_mnCom)
