def arithmetic_arranger(p,ansd=False):
    #check for lenght of problems
    if len(p) > 5:
        return "Error: Too many problems."
    
    a = [a.split()[0] for a in p]
    sym = [a.split()[1] for a in p]
    b = [a.split()[2] for a in p]

    #check for operator
    if "*" in sym or "/" in sym :
        return "Error: Operator must be '+' or '-'."
    
    #check for number
    for i in range(len(a)):
        if len(a[i]) > 4 or len(b[i]) > 4 :
            return f" Error: Numbers cannot be more than four digits. "
        if not a[i].isdigit() and b[i].isdigit():
            return "Error: Numbers must only contain digits."
    #arranement of numbers
    l1 = []
    l2 = []
    d = []
    ans = []
    
    for i in range(len(a)):
        if len(a[i]) > len(b[i]):
            l1.append(" "*2 + a[i])
        else:
            l1.append(" "*(len(b[i]) - len(a[i]) + 2) + a[i])

    for i in range(len(b)):
        if len(b[i]) > len(a[i]):
            l2.append(sym[i] + " " + b[i])
        else:
            l2.append(sym[i] + " "*(len(a[i]) - len(b[i]) + 1) + b[i])

    for i in range(len(a)):
        d.append("-"*(max(len(a[i]), len(b[i])) + 2))
    if ansd:
        for i in range(len(a)):
            if sym[i] == "+":
                anss = str(int(a[i]) + int(b[i]))
            else:
                anss = str(int(a[i]) - int(b[i]))

            if len(anss) > max(len(a[i]), len(b[i])):
                ans.append(" " + anss)
            else:
                ans.append(" "*(max(len(a[i]), len(b[i])) - len(anss) + 2) + anss)
        formatted = "    ".join(l1) + "\n" + "    ".join(l2) + "\n" + "    ".join(d) + "\n" + "    ".join(ans)
    else:
        formatted = "    ".join(l1) + "\n" + "    ".join(l2) + "\n" + "    ".join(d)
    return formatted

