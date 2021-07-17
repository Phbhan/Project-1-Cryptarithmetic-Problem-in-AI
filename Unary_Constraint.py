def unary_constraint(inp, dic):  # Unary constraints for each character and ''
    # Remove 0 in domain among the first candidates except c
    for i in inp[1:-1]:
        j = 0
        while(i[j] == ''):
            j += 1
        if(0 in dic[i[j]]):
            dic[i[j]].pop(0)

        dic[''] = [0]


def unary_constraint_for_c(inp, dic):  # Unary constraints for c0, c1, etc...
    for i in inp[0]:
        dic[i] = [v for v in range(0, 2)]
    for i in inp[len(inp) - 1]:
        dic[i] = [v for v in range(0, 2)]

    dic['c0'] = [0]


def unary_constraint_for_u(u):
    # Find values which not suitable for u
    tmpp = []
    for i in range(len(u)):
        for j in range(len(u[i])):
            tmp = 0
            for l in range(len(u[i][j]) - 2):
                tmp += u[i][j][l]
            if tmp % 10 != u[i][j][len(u[i][j]) - 2] or int(tmp/10) != u[i][j][len(u[i][j]) - 1]:
                tmpp.append(u[i][j])

    # Delete the unsuitable values for u
    for k in tmpp:
        for i in range(len(u)):
            for j in range(len(u[i])):
                if(u[i][j] == k):
                    u[i].pop(j)
                    break

    return u
