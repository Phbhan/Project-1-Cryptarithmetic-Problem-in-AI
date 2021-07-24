from copy import deepcopy
import Constraint as CSLib


class CSP:
    """
    A CSP consists of:
    domains     : a dictionary that maps each variable to its domain
    constraints : a list of constraints
    variables   : a set of variables
    """

    def __init__(self, variables, domains):  # Add more constraint is required

        self.variables = variables
        self.domains = domains
        self.value = {}
        self.constraint = CSLib.Constraint()

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
        return self.value[var]

    def set_value(self, var, value):
        self.value[var] = value

    def get_constraint(self):
        return self.constraint

    def get_all_values(self):
        return self.value
