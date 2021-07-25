def find_location_in_u(inp, x, u):
    # Returns format [[index_col1, index_row1], [index_col2, index_row2],...]
    # row and col are positions of letter x in inp -> detectable within u
    tmp = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == x:
                tmp.append([j, i])
                #since u moves from left to right and the first position on the column is for c

    return tmp


def find_neighbors(inp, x):  # Find neighbours of letter x

    neighbor = []

    for j in range(len(inp[0])):
        mark = False
        tmp = []
        for i in range(len(inp)):
            if inp[i][j] == x:
                mark = True
            else:
                tmp.append(inp[i][j])

        if mark == True:
            neighbor += tmp

    return neighbor
