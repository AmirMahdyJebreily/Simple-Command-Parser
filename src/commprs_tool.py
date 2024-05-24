def runNoRes(func, args):  # for run a func withou return any result
    func(args)


def splitArgs(arg, spliter = ','):
    res = []
    depth = 0
    target_depth = 0
    arg_n = 0
    res.append("")
    for i in range(0, len(arg)):
        if arg[i] == "(":
            old_depth = depth
            depth += 1
            if len(res) == 0 and old_depth == 0:
                target_depth = depth
        elif arg[i] == ")":
            depth -= 1
        elif arg[i] == spliter and depth == target_depth:
            arg_n += 1
            res.append("")
            continue
        if i != 0 and i != len(arg) - 1:
            res[arg_n] += arg[i]
    return res
