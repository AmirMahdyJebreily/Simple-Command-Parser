def runNoRes(func, args):  # for run a func withou return any result
    func(args)

def splitArgs(arg):
    res = []
    senscomma = True
    arg_n = 0
    res.append("")
    for i in range(0,len(arg)):
        if arg[i] == "(" and i != 0:
            senscomma = False
        elif arg[i] == ")":
            senscomma = True
        elif arg[i] == "," and senscomma != False:
            arg_n += 1
            res.append("")
            continue
        if i != 0 and i != len(arg) -1 :
            res[arg_n] += arg[i]
    return res

