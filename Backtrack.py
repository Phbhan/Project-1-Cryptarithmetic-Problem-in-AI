from copy import deepcopy
from math import floor
import CSP_Class as CSPLib


def Backtrack(assignment, csp, sign, result, mem):
    '''
    Apply backtrack to find answer
    assignment : a dictionary contains list of characters to be assigned alternately, index, length of collum and row
    csp        : csp variable
    sign       : list of signs in input
    result     : result of oparation in that collum
    mem        : the memorized value of that collum
    '''

    if isComplete(assignment):
        return True

    var = assignment['list'][assignment['index']]
    location = [int(floor(assignment['index'] / assignment['max_len'][1])),
                int(assignment['index'] % assignment['max_len'][1])]  # col, row
    constraint = csp.get_constraint()

    if location[1] == 0:  # At the first character in a collum
        result = 0
        mem = 0

    # Result positioning
    if assignment['max_len'][1] - location[1] == 2:
        if result in csp.get_domain(var):
            if (csp.get_value(var) == None and constraint.get_used(result) == False):
                csp.set_value(var, result)
                constraint.set_used(result, True)
                assignment['index'] += 1
                if Backtrack(assignment, csp, sign, result, mem) == True:
                    return True
                assignment['index'] -= 1
                constraint.set_used(result, False)
                csp.set_value(var, None)
            else:
                if csp.get_value(var) == result:
                    assignment['index'] += 1
                    if Backtrack(assignment, csp, sign, result, mem) == True:
                        return True
                    assignment['index'] -= 1
        return False

    # Memorized value location
    if assignment['max_len'][1] - location[1] == 1:
        remain = mem
        if var == 'c0' and not(mem == 0):
            return False
        csp.set_value(var, remain)
        assignment['index'] += 1
        if Backtrack(assignment, csp, sign, result, mem) == True:
            return True
        assignment['index'] -= 1
        csp.set_value(var, None)
        return False

    # Operand location
    if csp.get_value(var) == None:
        domain = csp.get_domain(var)
        for asg_value in domain:
            # Check whether considering value is used or not
            if constraint.get_used(asg_value) == False:
                constraint.set_used(asg_value, True)
                tmp = Assigned(location[1], sign, result, asg_value, mem)
                result = tmp[0]
                mem = tmp[1]
                csp.set_value(var, asg_value)
                assignment['index'] += 1
                if Backtrack(assignment, csp, sign, result, mem) == True:
                    return True
                assignment['index'] -= 1
                csp.set_value(var, None)
                tmp = reAssigned(location[1], sign, result, asg_value, mem)
                result = tmp[0]
                mem = tmp[1]
                constraint.set_used(asg_value, False)
    else:
        tmp = Assigned(location[1], sign, result, csp.get_value(var), mem)
        result = tmp[0]
        mem = tmp[1]
        assignment['index'] += 1
        if Backtrack(assignment, csp, sign, result, mem) == True:
            return True
        assignment['index'] -= 1
        tmp = reAssigned(location[1], sign, result, csp.get_value(var), mem)
        result = tmp[0]
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
