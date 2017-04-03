import pylp

def match(costs):

    n = costs.shape[0]
    m = costs.shape[1]

    num_variables = n*m
    objective = pylp.LinearObjective(num_variables)

    for i in range(n):
        for j in range(m):
            objective.set_coefficient(i*m+j, costs[i,j])

    constraints = pylp.LinearConstraints()

    for i in range(n):
        sum_to_one = pylp.LinearConstraint()
        for j in range(m):
            sum_to_one.set_coefficient(i*m+j, 1.0)
        sum_to_one.set_relation(pylp.Relation.LessEqual)
        sum_to_one.set_value(1.0)
        constraints.add(sum_to_one)

    for j in range(m):
        sum_to_one = pylp.LinearConstraint()
        for i in range(n):
            sum_to_one.set_coefficient(i*m+j, 1.0)
        sum_to_one.set_relation(pylp.Relation.LessEqual)
        sum_to_one.set_value(1.0)
        constraints.add(sum_to_one)

    solver = pylp.GurobiBackend()
    solver.initialize(num_variables, pylp.VariableType.Binary)
    solver.set_objective(objective)
    solver.set_constraints(constraints)

    solution = pylp.Solution()
    solver.solve(solution)

    matches = []
    for i in range(n):
        for j in range(m):
            if solution[i*m+j] > 0.5:
                matches.append((i,j))

    return matches
