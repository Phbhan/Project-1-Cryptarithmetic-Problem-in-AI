import Backtrack as BTLib
import CSP_Class as CSPLib
import Constraint as CSLib
import Multiply as BTMLib
from File import *
# rom Input import *


def main():
    inp,sign=readfile()
    mulSign = False


    dic = {}
    asg = {}
    asg_list = []

    # Initialize dic and assignment
    # dic: includes alphabets and their domains


    for traversal in sign:
        if (traversal == '*'):
            mulSign = True
    # Finds whether a single multiply operator exists


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
    if (mulSign): # If multiply operator found, do backtrack exclusively for multiply
        BTMLib.Backtrack_multiply(asg, ExeCSP, sign, q1=[], q2=[], result=0)
    else: # Otherwise, execute the normal backtrack
        BTLib.Backtracking(asg, ExeCSP, sign, 0, 0)
    print(ExeCSP.get_all_values())


main()