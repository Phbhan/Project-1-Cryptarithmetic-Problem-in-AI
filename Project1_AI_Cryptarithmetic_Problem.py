import Backtrack as BTLib
import CSP_Class as CSPLib
import Constraint as CSLib
import multiply as BTMLib
from File import *
import multiprocessing

# rom Input import *

WAITING_TIME = 7  # minutes


def main():
    inp, sign = readfile()
    mulSign = False

    # Initialize dic and assignment
    # dic: includes alphabets and their domains

    for traversal in sign:
        if (traversal == '*'):
            mulSign = True
    # Finds whether a single multiply operator exists

    domain = {}
    asg_list = []

    for j in range(len(inp[0]) - 1, -1, -1):
        for i in range(len(inp)):
            if(inp[i][j] != ''):
                domain[inp[i][j]] = [v for v in range(0, 10)]
            else:
                domain[inp[i][j]] = [0]
            asg_list.append(inp[i][j])

    asg = {}
    asg['list'] = asg_list
    asg['index'] = 0
    asg['max_len'] = [len(inp[0]), len(inp)]

    variables = []
    for i in domain:
        variables.append(i)
    ExeCSP = CSPLib.CSP(variables, domain)

    ExeCSP.get_constraint().unary_constraint(inp, domain)

    if (mulSign):  # If multiply operator found, do backtrack exclusively for multiply
        BTMLib.Backtrack_multiply(asg, ExeCSP, q1=[], q2=[], result=0)
    else:  # Otherwise, execute the normal backtrack
        if BTLib.Backtrack(asg, ExeCSP, sign, 0, 0)==False: 
            print("No solution")
            savefile("No solution")
            return

    print(ExeCSP.get_all_values())
    savefile(ExeCSP.get_all_values())


# main()
if __name__ == '__main__':
    t = WAITING_TIME*60
    p = multiprocessing.Process(target=main)
    p.start()
    p.join(t)
    if p.is_alive():
        p.terminate()
        print("No solution")
        savefile("No solution")
        p.join()
