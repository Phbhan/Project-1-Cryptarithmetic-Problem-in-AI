import Constraint_Class_Functions as CTLib
import Remover as remoLib


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
                if remoLib.remove_same_value_of_operand_from_u(
                        u, location[0], location[1], value):
                    revise = True
    return revise


def check_empty_col_in_u(u):
    # Check if there exists a column without appropriate value within u
    for i in u:
        if i == []:
            return True
    return False