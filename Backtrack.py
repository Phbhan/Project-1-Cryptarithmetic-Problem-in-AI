import Constraint_Class_Functions as CTLib
import Remover as remoLib
import AC3_Functions as AC3Lib
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
        remoLib.remove_diff_value_of_operand_from_u(u, l[0], l[1], value)

    queue = []
    for q in csp.get_constraints(var).get_neighbors():
        queue.append([var, q])
    return AC3Lib.AC3(csp, queue, u, assignment)


def isComplete(assignment):
    # Check whether Backtrack is done
    for v in assignment:
        if assignment[v] == -1:
            return False
    return True
