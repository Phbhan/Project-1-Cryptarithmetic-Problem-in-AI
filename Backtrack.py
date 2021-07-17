import Constraint_Class_Functions as CTLib
import Remover as remoLib
import copy


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
                CTLib.used[value] = True
            if Inference(assignment, csp, var, value, temp) == True:
                result = Backtracking(assignment, csp, temp)
                if result != False:
                    return result

        # Recover previous action if recently considered value is not suitable with var
            if csp.get_constraints(var).get_type() == 1:
                CTLib.used[value] = False
    assignment[var] = -1
    csp.set_unassigned_variable(var)
    return False


def Inference(assignment, csp, var, value, u):
    location = csp.get_constraints(var).get_locations()
    for l in location:
        remoLib.remove_diff_value_of_sohang_from_u(u, l[0], l[1], value)

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
                if remoLib.remove_same_value_of_sohang_from_u(
                        u, location[0], location[1], value):
                    revise = True
    return revise


def isComplete(assignment):
    # Check whether Backtrack is done
    for v in assignment:
        if assignment[v] == -1:
            return False
    return True


def check_empty_col_in_u(u):
    # Check if there exists a column without appropriate value within u
    for i in u:
        if i == []:
            return True
    return False
