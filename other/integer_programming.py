# -*- coding: utf-8 -*-
"""

@author: costa

Simple Primal Dual Example.
"""


from gurobipy import Model, GRB, quicksum

print(""" (a) part of the problem \n\n""")

model = Model()

# Set Variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = model.addVar(vtype=GRB.CONTINUOUS, name='x2')
array = [x1,x2]

model.update()

# Set objective
model.setObjective(
    2*x1 - 4*x2,
    GRB.MINIMIZE
)
model.update()

# Set constraints
model.addConstr(2*x1 + x2 <= 5)
model.addConstr(-4*x1 + 4*x2 <= 5)
model.addConstr(x1 <= 1)
model.addConstr(x2 <= 2)
model.addConstr(x1 <= 0)


model.update()
model.optimize()
print(array)