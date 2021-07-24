import Backtrack as BTLib
import CSP_Class as CSPLib
import Constraint as CSLib
# rom Input import *


def main():
    # sign = ['+', '-', '+']
    # inp = [['c2', 'c1', 'c0'], ['A', 'A', 'B'], [
    #     '', 'C', 'A'], ['', 'B', 'A'], ['', 'D', 'B'], ['c0', 'c2', 'c1']]
    sign = ['+', '+']
    inp = [['c4', 'c3', 'c2', 'c1', 'c0'], ['', 'S', 'E', 'N', 'D'], [
        '', 'M', 'O', 'R', 'E'], ['M', 'O', 'N', 'E', 'Y'], ['c0', 'c4', 'c3', 'c2', 'c1']]


    #hey girl, input like this:
    #inp,sign=readfile()


    
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

    BTLib.Backtracking(asg, ExeCSP, sign, 0, 0)
    print(ExeCSP.get_all_values())


main()
