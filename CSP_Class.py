from copy import deepcopy
import Constraint as CSLib


class CSP:
    """
    A CSP consists of:
    variables   : a set of variables
    domains     : a dictionary that maps each variable to its domain
    constraints : a list of constraints
    values     : a dictionary that maps each variable to its value
    """

    def __init__(self, variables, domains):  # Add more constraint is required

        self.variables = variables
        self.domains = domains
        self.constraint = CSLib.Constraint()

        self.value = {}
        for i in variables:
            self.value[i] = None
        self.value[''] = 0
        self.value['c0'] = 0

    def get_domain(self, var):
        '''
        Get domain of variable var
        '''
        return self.domains[var]

    def get_value(self, var):
        '''
        Get value of variable var
        '''
        return self.value[var]

    def set_value(self, var, value):
        '''
        Set value for variable var
        '''
        self.value[var] = value

    def get_constraint(self):
        '''
        Get constraint
        '''
        return self.constraint

    def get_all_values(self):
        '''
        Get values of all variable
        '''
        return self.value
