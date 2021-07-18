import copy


def Recursion(k, tmp, dic, index, u, check, used):  # Recursion used to initialize array u
    if(k == len(index)):
        u.append(tmp.copy())
        return

    if check[index[k]] == None:
        for i in dic[index[k]]:
            if len(index[k]) == 1:
                if used[i] == False:
                    check[index[k]] = i
                    used[i] = True
                    tmp.append(i)
                    Recursion(k+1, tmp, dic, index, u, check, used)
                    check[index[k]] = None
                    used[i] = False
                    tmp.pop()
            else:
                check[index[k]] = i
                tmp.append(i)
                Recursion(k+1, tmp, dic, index, u, check, used)
                check[index[k]] = None
                tmp.pop()
    else:
        tmp.append(check[index[k]])
        Recursion(k+1, tmp, dic, index, u, check, used)
        tmp.pop()


def binarize(inp, dic):
    u = [[] for x in range(len(inp[0]))]
    tmp = []
    index = []
    check = {}
    used = {}
    for j in range(len(inp[0]) - 1, -1, -1):  # Xét từ cột phải nhất qua trái
        for i in range(len(inp)):
            check[inp[i][j]] = None
            for q in range(0, 10):
                used[q] = False
            index.append(inp[i][j])  # Gather each alphabet
        Recursion(0, tmp, dic, index, u[j], check, used)
        tmp.clear()
        index.clear()
    return u
