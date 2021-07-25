used = []
for v in range(0, 10):
    used.append(False)


class Constraint:

    def __init__(self, neightbors, locations, my_type):
        self.neighbors = neightbors
        self.locations = locations
        self.type = my_type        # type = 0 is c, type = 1 is normal operand

    def isConsistent(self, value, u):
        if find_value_constraint(u, value, self.locations) == False:
            return False
        if self.type == 1:
            return all_diff_constraint(value)
        return True

    def display(self):
        print(self.neighbors)
        print(self.locations)
        print(self.type)

    def get_neighbors(self):
        return self.neighbors

    def get_locations(self):
        return self.locations

    def get_type(self): return self.type


def all_diff_constraint(value):  # Constraint for class Constraint
    # Check whether value is assigned prior before
    return not(used[value])


def find_value_constraint(u, value, locations): # Constraint for class Constraint
    # Traverse within u in search for any variable having the same as value
    for index in locations:
        check = False
        for i in u[index[0]]:
            if i[index[1]] == value:
                check = True
        if check == False:
            return False
    return True

