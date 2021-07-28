
class Constraint:
    '''
    A Constraint consists of:
    used: a list of boolean values indicate whether or not that number is assigned 
    '''

    def __init__(self):
        self.used = []
        for v in range(0, 10):
            self.used.append(False)

    def get_used(self, var):
        '''
        Get boolean values of used
        '''
        return self.used[var]

    def set_used(self, var, value):
        '''
        Set True/False for index var in used
        '''
        self.used[var] = value

    # Unary constraints for each character and ''
    def unary_constraint_for_operand(self, inp, domain):
        '''
        Apply unary constraint for operand
        inp   : list of input character
        domain: a dictionary map the character to its domain
        '''
        # Remove 0 in domain among the first candidates except c
        for i in inp[1:-1]:
            j = 0
            while(i[j] == ''):
                j += 1
            if(0 in domain[i[j]]):
                domain[i[j]].pop(0)
        domain[''] = [0]

    # Unary constraints for c0, c1, etc...
    def unary_constraint_for_c(self, inp, domain):
        '''
        Apply unary constraint for memorized operand
        inp   : list of input character
        domain: a dictionary map the character to its domain
        '''
        for i in inp[0]:
            domain[i].clear()
        domain['c0'] = [0]

    def unary_constraint(self, inp, domain):
        '''
        Apply unary constraint for domain
        inp   : list of input character
        domain: a dictionary map the character to its domain
        '''
        self.unary_constraint_for_operand(inp, domain)
        self.unary_constraint_for_c(inp, domain)
