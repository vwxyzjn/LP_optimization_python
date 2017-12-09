# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:31:31 2017

@author: costa
"""

from gurobipy import Model, GRB, quicksum

mu = 4

print("=====================================\n\n Primal: \n\n")
model = Model()

# Set Variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = model.addVar(vtype=GRB.CONTINUOUS, name='x2')

model.update()
    
# Set objective
model.setObjective(10*x1 + 11*x2, GRB.MINIMIZE)
model.update()

# Set constraints
model.addConstr(mu*2*x1 + mu*3*x2 == mu*2)
model.addConstr(3*x1 + 4*x2 == 3)


model.update()
model.optimize()
print(x1,x2)


print("=====================================\n\n Dual: \n\n")
model = Model()

# Set Variables
y1 = model.addVar(vtype=GRB.CONTINUOUS, name='y1', lb=-1e20)
y2 = model.addVar(vtype=GRB.CONTINUOUS, name='y2', lb=-1e20)

model.update()
    
# Set objective
model.setObjective(mu*2*y1 + 3*y2, GRB.MAXIMIZE)
model.update()

# Set constraints
model.addConstr(mu*2*y1 + 3*y2 <= 10)
model.addConstr(mu*3*y1 + 4*y2 <= 11)


model.update()
model.optimize()
print(y1,y2)