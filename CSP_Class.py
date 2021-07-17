import copy


class CSP:
    """
    A CSP consists of:
    domains     : a dictionary that maps each variable to its domain
    constraints : a list of constraints
    variables   : a set of variables
    """

    def __init__(self, variables, domains, constraints):  # Add more constraint is required

        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.value = {}

        self.unassigned = variables.copy()

    def get_unassigned_variable(self):
        return self.unassigned.pop(0)

    def set_unassigned_variable(self, var):
        self.unassigned.insert(0, var)

    def get_domain(self, var):
        '''
        Get domain of variable var
        '''
        return self.domains[var]

    def get_constraints(self, var):
        return self.constraints[var]

    def get_domains(self):
        ''' 
        Get the whole domain of CSP
        '''
        return self.domains

    def remove_from_domain(self, var, value):
        self.domains[var].remove(value)

    def set_domains(self, domains):
        self.domains = copy.deepcopy(domains)
