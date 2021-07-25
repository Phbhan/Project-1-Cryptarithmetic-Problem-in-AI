import CSP_Class as CSPLib
import Constraint as CSLib
from math import floor


def isComplete(asg):
    # Check whether Backtrack is done
    return asg['index'] == len(asg['list'])


def get_result(q1, q2, result, col):
    tmp = col
    index_1 = 0
    index_2 = col
    ans = result
    while index_1 <= col and index_2 >= 0:
        ans += q1[index_1] * q2[index_2]
        index_1 += 1
        index_2 -= 1
    return ans


def Backtrack_multiply(assignment, csp, sign, q1, q2, result):
    if isComplete(assignment):
        return True

    var = assignment['list'][assignment['index']]
    location = [int(floor(assignment['index'] / assignment['max_len'][1])),
                int(assignment['index'] % assignment['max_len'][1])]  # col, row
    constraint = csp.get_constraint()

    # Vị trí kết quả
    if assignment['max_len'][1] - location[1] == 2:
        print(q1, q2)
        tmp_result = int(get_result(q1, q2, result, location[0]) % 10)
        print('result', tmp_result)
        if tmp_result in csp.get_domain(var):
            print(csp.get_value(var))
            if (csp.get_value(var) == None and constraint.get_used(tmp_result) == False):
                csp.set_value(var, tmp_result)
                constraint.set_used(tmp_result, True)
                assignment['index'] += 1
                if Backtrack_multiply(assignment, csp, sign, q1, q2, result) == True:
                    return True
                assignment['index'] -= 1
                constraint.set_used(tmp_result, False)
                csp.set_value(var, None)
            elif csp.get_value(var) == tmp_result:
                assignment['index'] += 1
                if Backtrack_multiply(assignment, csp, sign, q1, q2, result) == True:
                    return True
                assignment['index'] -= 1
        return False

    if assignment['max_len'][1] - location[1] == 1:  # Vị trí số nhớ
        remain = int(floor(get_result(q1, q2, result, location[0]) / 10))
        if var == 'c0' and not(remain == 0):
            return False
        csp.set_value(var, remain)
        assignment['index'] += 1
        if Backtrack_multiply(assignment, csp, sign, q1, q2, remain):
            return True
        assignment['index'] -= 1
        csp.set_value(var, None)
        return False

    if csp.get_value(var) == None:
        domain = csp.get_domain(var)
        for i in domain:
            # Kiểm tra số đang xét có được dùng chưa
            if constraint.get_used(i) == False:
                constraint.set_used(i, True)
                if location[1] == 1:
                    q1.append(i)
                elif location[1] == 2:
                    q2.append(i)
                csp.set_value(var, i)
                assignment['index'] += 1
                if Backtrack_multiply(assignment, csp, sign, q1, q2, result) == True:
                    return True
                assignment['index'] -= 1
                if location[1] == 1:
                    q1.pop(-1)
                elif location[1] == 2:
                    q2.pop(-1)
                csp.set_value(var, None)
                constraint.set_used(i, False)
    else:
        if location[1] == 1:
            q1.append(csp.get_value(var))
        elif location[1] == 2:
            q2.append(csp.get_value(var))
        assignment['index'] += 1
        if Backtrack_multiply(assignment, csp, sign, q1, q2, result) == True:
            return True
        assignment['index'] -= 1
        if location[1] == 1:
            q1.pop(-1)
        elif location[1] == 2:
            q2.pop(-1)
    return False


def main_multiply():
    # sign = ['+', '-', '+']
    # inp = [['c2', 'c1', 'c0'], ['A', 'A', 'B'], [
    #     '', 'C', 'A'], ['', 'B', 'A'], ['', 'D', 'B'], ['c0', 'c2', 'c1']]
    sign = ['+', '*']
    inp = [['c4', 'c3', 'c2', 'c1', 'c0'], ['', '', 'A', 'B', 'C'], [
        '', '', '', 'D', 'E'], ['A', 'F', 'C', 'G', 'H'], ['c0', 'c4', 'c3', 'c2', 'c1']]

    dic = {}
    asg = {}
    asg_list = []

    # Initialize dic and assignment
    # dic: includes alphabets and their domains

    for j in range(len(inp[0]) - 1, -1, -1):
        for i in range(len(inp)):
            if(inp[i][j] != ''):
                dic[inp[i][j]] = [v for v in range(0, 10)]
            else:
                dic[inp[i][j]] = [0]
            asg_list.append(inp[i][j])

    asg['list'] = asg_list
    asg['index'] = 0
    asg['max_len'] = [len(inp[0]), len(inp)]

    CSLib.unary_constraint(inp, dic)
    csp_list = []
    for i in dic:
        csp_list.append(i)
    ExeCSP = CSPLib.CSP(csp_list, dic)
    Backtrack_multiply(asg, ExeCSP, sign, q1=[], q2=[], result=0)
    print(ExeCSP.get_all_values())


main_multiply()
