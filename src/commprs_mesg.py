__messagesCodes: {
    0: "OK",
    1: "Warning",
    2: "SyntaxErr",
    3: "IdentifyErr",
} # type: ignore

def message(code, content):
    return ": " + "["+ __messagesCodes[code] +"] " + content