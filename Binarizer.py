def Recursion(k, tmp, dic, index, u):  # Recursion used to initialize array u
    if(k == len(index)):
        tmpp = tmp.copy()
        u.append(tmpp)
        return

    for i in dic[index[k]]:
        tmp.append(i)
        Recursion(k+1, tmp, dic, index, u)
        tmp.pop()


def binarize(inp, dic):
    u = [[] for x in range(len(inp[0]))]
    tmp = []
    index = []
    for j in range(len(inp[0]) - 1, -1, -1):
        for i in range(len(inp)):
            index.append(inp[i][j])  # Gather each alphabet
        Recursion(0, tmp, dic, index, u[j])
        tmp.clear()
        index.clear()

    return u

