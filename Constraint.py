
class Constraint:

    def __init__(self):
        self.used = []
        for v in range(0, 10):
            self.used.append(False)

    def get_type(self):
        return self.type

    def get_used(self, var):
        return self.used[var]

    def set_used(self, var, value):
        self.used[var] = value


# Unary constraints for each character and ''
def unary_constraint_for_operand(inp, dic):
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
        dic[i].clear()

    dic['c0'] = [0]


def unary_constraint(inp, dic):
    unary_constraint_for_operand(inp, dic)
    unary_constraint_for_c(inp, dic)
