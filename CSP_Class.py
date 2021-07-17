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

    def display(self):
        print(self.variables)
        print(self.domains)
        print(self.value)

    def get_unassigned_variable(self):
        return self.unassigned.pop(0)

    def set_unassigned_variable(self, var):
        self.unassigned.insert(0, var)

    def get_domain(self, var):
        return self.domains[var]

    def get_constraints(self, var):
        return self.constraints[var]