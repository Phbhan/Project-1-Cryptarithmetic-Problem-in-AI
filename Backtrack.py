from copy import deepcopy
from math import floor
import CSP_Class as CSPLib


def Backtracking(assignment, csp, sign, value, mem):
    if isComplete(assignment):
        return True

    var = assignment['list'][assignment['index']]
    location = [int(floor(assignment['index'] / assignment['max_len'][1])),
                int(assignment['index'] % assignment['max_len'][1])]  # col, row
    constraint = csp.get_constraint()

    if location[1] == 0:
        value = 0
        mem = 0

    # Result position
    if assignment['max_len'][1] - location[1] == 2:
        result = value
        if result in csp.get_domain(var):
            if (csp.get_value(var) == None and constraint.get_used(result) == False):
                csp.set_value(var, result)
                constraint.set_used(value, True)
                assignment['index'] += 1
                if Backtracking(assignment, csp, sign, value, mem) == True:
                    return True
                assignment['index'] -= 1
                constraint.set_used(value, False)
                csp.set_value(var, None)
            else:
                if csp.get_value(var) == result:
                    assignment['index'] += 1
                    if Backtracking(assignment, csp, sign, value, mem) == True:
                        return True
                    assignment['index'] -= 1

        return False

    if assignment['max_len'][1] - location[1] == 1:  # Memorized value position
        remain = mem
        if var == 'c0' and not(mem == 0):
            return False
        csp.set_value(var, remain)
        assignment['index'] += 1
        if Backtracking(assignment, csp, sign, value, mem) == True:
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
                tmp = Assigned(location[1], sign, value, i, mem)
                value = tmp[0]
                mem = tmp[1]
                csp.set_value(var, i)
                assignment['index'] += 1
                if Backtracking(assignment, csp, sign, value, mem) == True:
                    return True
                assignment['index'] -= 1
                csp.set_value(var, None)
                tmp = reAssigned(location[1], sign, value, i, mem)
                value = tmp[0]
                mem = tmp[1]
                constraint.set_used(i, False)
    else:
        tmp = Assigned(location[1], sign, value, csp.get_value(var), mem)
        value = tmp[0]
        mem = tmp[1]
        assignment['index'] += 1
        if Backtracking(assignment, csp, sign, value, mem) == True:
            return True
        assignment['index'] -= 1
        tmp = reAssigned(location[1], sign, value, csp.get_value(var), mem)
        value = tmp[0]
        mem = tmp[1]
    return False


def isComplete(asg):
    # Check whether Backtrack is done
    return asg['index'] == len(asg['list'])


def Assigned(k, sign, result, value, mem):
    if k == 0 or sign[k-1] == '+':
        result += value
        if result > 9:
            result -= 10
            mem += 1
    else:
        if result - value < 0:
            result = result + 10
            mem -= 1
        result -= value
    return [result, mem]


def reAssigned(k, sign, result, value, mem):
    if k == 0 or sign[k-1] == '+':
        if result - value < 0:
            result = result + 10
            mem -= 1
        result -= value
    else:
        result += value
        if result > 9:
            result -= 10
            mem += 1
    return [result, mem]
