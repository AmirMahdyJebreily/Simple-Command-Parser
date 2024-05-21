__messagesCodes = {
    0: "OK",
    1: "Warning",
    2: "SyntaxErr",
    3: "IdentifyErr",
    4: "ArgsErr",
}  # type: ignore

__defaultContents = {
    0: "",
    1: "There is a problem",
    2: "The syntax is not valid",
    3: "This command has no meaning and has never been defined",
    4: "Arguments entered incorrectly"
}


def message(code, content="@default@"):
    print(
        "~ "
        + "["
        + __messagesCodes[code]
        + "] "
        + content.replace("@default@", __defaultContents[code])
    )
