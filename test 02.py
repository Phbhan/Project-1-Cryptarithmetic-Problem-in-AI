import copy

used = []
for v in range(0, 10):
    used.append(False)


class CSP:
    """
    A CSP consists of:
    domains     : a dictionary that maps each variable to its domain
    constraints : a list of constraints
    variables   : a set of variables
    """

    def __init__(self, variables, domains, constraints):  # cần thêm constraint

        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.value = {}

        self.unassigned = variables.copy()

    def display(self):
        print(self.variables)
        print(self.domains)
        # print(self.constraints.display())
        print(self.value)

    def get_unassigned_variable(self):
        return self.unassigned.pop(0)

    def set_unassigned_variable(self, var):
        self.unassigned.insert(0, var)

    def get_domain(self, var):
        return self.domains[var]

    def get_constraints(self, var):
        return self.constraints[var]


class Constraint:

    def __init__(self, neightbors, locations, my_type):
        self.neighbors = neightbors
        self.locations = locations
        self.type = my_type        # type = 0 là c, type = 1 là số hạng thường

    def isConsistent(self, value, u):
        # print('in consistent', self.type, '312asdda',
        #       self.locations, 'sadadfa', self.neighbors)
        if find_value_constraint(u, value, self.locations) == False:
            ##print('cannot find value', value)
            return False
        if self.type == 1:
            return all_diff_constraint(value)
        return True

    def display(self):
        print(self.neighbors)
        print(self.locations)
        print(self.type)

    def get_neighbors(self):
        return self.neighbors

    def get_locations(self):
        return self.locations

    def get_type(self): return self.type


def all_diff_constraint(value):  # Constraint dành cho class Constraint
    # Check value đã được assigned trước đó chưa
    return not(used[value])


# Constraint dành cho class Constraint
def find_value_constraint(u, value, locations):
    # Tìm trong u có cái nào = value không
    for index in locations:
        check = False
        for i in u[index[0]]:
            if i[index[1]] == value:
                check = True
        if check == False:
            return False
    return True


def Recursion(k, tmp, dic, index, u):  # dùng đệ quy để tạo ra u
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
            index.append(inp[i][j])  # lấy các chữ cái
        Recursion(0, tmp, dic, index, u[j])
        tmp.clear()
        index.clear()

    return u


def unary_constraint(inp, dic):  # unary constraints cho các chữ và ''
    # bỏ số 0 trong domain của những chữ đứng đầu trừ c
    for i in inp[1:-1]:
        j = 0
        while(i[j] == ''):
            j += 1
        if(0 in dic[i[j]]):
            dic[i[j]].pop(0)

        dic[''] = [0]


def unary_constraint_for_c(inp, dic):  # unary constraints cho các c0, c1, ...
    for i in inp[0]:
        dic[i] = [v for v in range(0, 2)]
    for i in inp[len(inp) - 1]:
        dic[i] = [v for v in range(0, 2)]

    dic['c0'] = [0]


def unary_constraint_for_u(u):
    # tìm các giá trị không thỏa trong u
    tmpp = []
    for i in range(len(u)):
        for j in range(len(u[i])):
            tmp = 0
            for l in range(len(u[i][j]) - 2):
                tmp += u[i][j][l]
            if tmp % 10 != u[i][j][len(u[i][j]) - 2] or int(tmp/10) != u[i][j][len(u[i][j]) - 1]:
                tmpp.append(u[i][j])

    # delete các giá trị không thỏa trong u
    for k in tmpp:
        for i in range(len(u)):
            for j in range(len(u[i])):
                if(u[i][j] == k):
                    u[i].pop(j)
                    break

    return u


# Loại bỏ những giá trị không bằng value ở vị trí đã cho trong inp tại u
def remove_diff_value_of_sohang_from_u(u, index_col, index_row, value):
    tmp = []
    for i in u[index_col]:
        # print(i)
        u = u
        if i[index_row] != value:
            tmp.append(i)

    for i in tmp:
        u[index_col].remove(i)

    return u


# Loại bỏ những giá trị bằng value ở vị trí đã cho trong inp tại u
def remove_same_value_of_sohang_from_u(u, index_col, index_row, value):
    tmp = []
    for i in u[index_col]:
        u = u
        if i[index_row] == value:
            tmp.append(i)

    if(len(tmp) == 0):
        return False  # Không có số giống số yêu cầu

    for i in tmp:
        u[index_col].remove(i)
    return True


def find_location_in_u(inp, x, u):
    # Trả về dạng [[index_col1, index_row1], [index_col2, index_row2],...]
    # row và col là vị trí của chữ x trong inp -> dò được trong u
    tmp = []
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if inp[i][j] == x:
                tmp.append([j, i])
                # vì u đi từ trái qua và vị trí đầu tiên trên cột là dành cho c

    return tmp


def find_neighbors(inp, x):  # Tìm neighbors của chữ x

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


def Backtracking(assignment, csp, u):
    if isComplete(assignment):
        return assignment

    var = csp.get_unassigned_variable()
    domain = csp.get_domain(var).copy()

    for value in domain:

        temp = copy.deepcopy(u)
        if csp.get_constraints(var).isConsistent(value, temp):
            assignment[var] = value
            if csp.get_constraints(var).get_type() == 1:
                used[value] = True
            if Inference(assignment, csp, var, value, temp) == True:
                result = Backtracking(assignment, csp, temp)
                if result != False:
                    return result

        # Hồi phục những gì đã làm nếu giá trì vừa gán không phù hợp với var
            if csp.get_constraints(var).get_type() == 1:
                used[value] = False
    assignment[var] = -1
    csp.set_unassigned_variable(var)
    return False


def Inference(assignment, csp, var, value, u):
    location = csp.get_constraints(var).get_locations()
    for l in location:
        remove_diff_value_of_sohang_from_u(u, l[0], l[1], value)

    queue = []
    for q in csp.get_constraints(var).get_neighbors():
        queue.append([var, q])
    return AC3(csp, queue, u, assignment)


def AC3(csp, queue, u, assignment):
    while not(queue == []):
        uv = queue.pop(0)
        v = uv[1]
        if not (assignment[v] == -1):
            continue
        if Revise(csp, v, u):
            if check_empty_col_in_u(u):
                return False
            neighbor = csp.get_constraints(
                v).get_neighbors().copy()
            neighbor.remove(uv[0])
            for q in neighbor:
                queue.append([v, q])
    return True


def Revise(csp, v, u):
    revise = False
    for value in csp.get_domain(v):
        if not csp.get_constraints(v).isConsistent(value, u):
            for location in csp.get_constraints(v).get_locations():
                if remove_same_value_of_sohang_from_u(
                        u, location[0], location[1], value):
                    revise = True
    return revise


def isComplete(assignment):
    # Kiểm tra hoàn thành Backtrack
    for v in assignment:
        if assignment[v] == -1:
            return False
    return True


def check_empty_col_in_u(u):
    # Kiểm tra trong u có cột nào không có giá trị
    for i in u:
        if i == []:
            return True
    return False


def main():
    inp = [['c4', 'c3', 'c2', 'c1', 'c0'], ['', 's', 'e', 'n', 'd'], [
        '', 'm', 'o', 'r', 'e'], ['m', 'o', 'n', 'e', 'y'], ['c0', 'c4', 'c3', 'c2', 'c1']]
    #inp = [['c1', 'c0'], ['a', 'b'], ['', 'c'], ['a', 'd'], ['c0', 'c1']]
    # inp = [['c3', 'c2', 'c1', 'c0'], ['', 't', 'w', 'o'], [
    #     '', 't', 'w', 'o'], ['f', 'o', 'u', 'r'], ['c0', 'c3', 'c2', 'c1']]

    dic = {}
    assignment = {}

    # Khởi tạo dic và assignment
    # dic: chứa chữ và domain của nó
    # assignment: dùng cho Backtrack
    for j in range(len(inp[0]) - 1, -1, -1):
        for i in range(len(inp)):
            if(inp[i][j] != ''):
                dic[inp[i][j]] = [v for v in range(0, 10)]
            else:
                dic[inp[i][j]] = [0]
            assignment[inp[i][j]] = -1

    # Dùng unary constraint để loại bỏ những giá trị không phù hợp trong domain ở dic
    unary_constraint(inp, dic)
    unary_constraint_for_c(inp, dic)

    # Đưa n-ary constraints về binary constraints thông qua ma trận u trung gian
    u = binarize(inp, dic)
    u = unary_constraint_for_u(u)  # u sẽ bắt đầu từ cột đầu đi qua phải

    # Khởi tạo constraint cho các variables
    con = {}
    for var in dic:
        if(len(var) == 1):
            con[var] = Constraint(find_neighbors(
                inp, var), find_location_in_u(inp, var, u), 1)
        else:
            con[var] = Constraint(find_neighbors(
                inp, var), find_location_in_u(inp, var, u), 0)

    # Khởi tạo CSP
    ez_game = CSP([var for var in dic], dic, con)

    # Thực hiện Backtrack
    print(Backtracking(assignment, ez_game, u))


main()
