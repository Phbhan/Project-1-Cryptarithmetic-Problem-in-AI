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

    # Result position
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

    if assignment['max_len'][1] - location[1] == 1:  # Memorized value position
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
            # Check whether considering value is appropriate 
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

