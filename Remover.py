# Eliminate variables which do not share the same amount as value at position given in inp at u
def remove_diff_value_of_operand_from_u(u, index_col, index_row, value):
    tmp = []
    for i in u[index_col]:
        # print(i)
        u = u
        if i[index_row] != value:
            tmp.append(i)

    for i in tmp:
        u[index_col].remove(i)

    return u


# Eliminate variables share the same amount as value at position given in inp at u
def remove_same_value_of_operand_from_u(u, index_col, index_row, value):
    tmp = []
    for i in u[index_col]:
        u = u
        if i[index_row] == value:
            tmp.append(i)

    if(len(tmp) == 0):
        return False  # No equal value given found

    for i in tmp:
        u[index_col].remove(i)
    return True
