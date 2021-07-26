import Backtrack as BTLib
import CSP_Class as CSPLib
import Constraint as CSLib
import multiply as BTMLib
from Input import *
import multiprocessing
import time



WAITING_TIME = 7 #minutes



def main():
    # sign = ['+', '-', '+']
    # inp = [['c2', 'c1', 'c0'], ['A', 'A', 'B'], [
    #     '', 'C', 'A'], ['', 'B', 'A'], ['', 'D', 'B'], ['c0', 'c2', 'c1']]
    # sign = ['+', '+']
    # inp = [['c4', 'c3', 'c2', 'c1', 'c0'], ['', 'S', 'E', 'N', 'D'], [
    #     '', 'M', 'O', 'R', 'E'], ['M', 'O', 'N', 'E', 'Y'], ['c0', 'c4', 'c3', 'c2', 'c1']]
    

    inp,sign=readfile()
    mulSign = False
    
    dic = {}
    asg = {}
    asg_list = []

    for traversal in sign:
        if (traversal == '*'):
            mulSign = True
    

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
    if (mulSign):
        BTMLib.Backtrack_multiply(asg, ExeCSP, sign, q1=[], q2=[], result=0)
    else:
        BTLib.Backtracking(asg, ExeCSP, sign, 0, 0)
    print(ExeCSP.get_all_values())
    savefile(ExeCSP.get_all_values())

# main()




if __name__ == '__main__':
    t=WAITING_TIME*60
    p = multiprocessing.Process(target=main)
    p.start()
    p.join(t)
    if p.is_alive():
        p.terminate()
        print("No result")
        p.join()

