import copy
from Input import *
import CSP_Class as CSPLib
import Constraint_Class_Functions as CTLib
import Unary_Constraint as UCLib
import Backtrack as BTLib
import Finder as findLib


def Recursion(k, tmp, dic, index, u):  # Recursion used to initialize array u
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
            index.append(inp[i][j])  # Gather each alphabet
        Recursion(0, tmp, dic, index, u[j])
        tmp.clear()
        index.clear()

    return u


def main():
    inp = ReadFile()

    dic = {}
    assignment = {}

    # Initialize dic and assignment
    # dic: includes alphabets and their domains
    # assignement: used to aid Backtrack algorithm
    for j in range(len(inp[0]) - 1, -1, -1):
        for i in range(len(inp)):
            if(inp[i][j] != ''):
                dic[inp[i][j]] = [v for v in range(0, 10)]
            else:
                dic[inp[i][j]] = [0]
            assignment[inp[i][j]] = -1

    # Use unary constraint to remove unsuitable values in domain within dic
    UCLib.unary_constraint(inp, dic)
    UCLib.unary_constraint_for_c(inp, dic)

    # Transform n-ary constraints to binary constraints through matrix u as the intermediary
    u = binarize(inp, dic)
    u = UCLib.unary_constraint_for_u(u) # u will start from first column to the right

    # Initialize constraints for variables
    con = {}
    for var in dic:
        if(len(var) == 1):
            con[var] = CTLib.Constraint(findLib.find_neighbors(
                inp, var), findLib.find_location_in_u(inp, var, u), 1)
        else:
            con[var] = CTLib.Constraint(findLib.find_neighbors(
                inp, var), findLib.find_location_in_u(inp, var, u), 0)

    # Initialize CSP
    CSPExe = CSPLib.CSP([var for var in dic], dic, con)

    # Execute Backtrack
    SaveFile(BTLib.Backtracking(assignment, CSPExe, u))


main()

