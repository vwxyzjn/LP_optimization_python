# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:11:27 2017

@author: shuang
"""

from gurobipy import *

print("=====================================\n\n Primal: \n\n")
model = Model()

# Set Variables
y1 = model.addVar(vtype=GRB.CONTINUOUS, name='y1')
y2 = model.addVar(vtype=GRB.CONTINUOUS, name='y2')
y3 = model.addVar(vtype=GRB.CONTINUOUS, name='y3')
y4 = model.addVar(vtype=GRB.CONTINUOUS, name='y4')
    
model.update()
    
# Set objective
model.setObjective(quicksum([1.25 * y1, 2 * y2, y3, 4* y4]), GRB.MINIMIZE)
model.update()

# Set constraints
c1 = model.addConstr(quicksum([400*y1, 200*y2, 150*y3, 500*y4]) >= 2000)
c2 = model.addConstr(quicksum([3*y1, 2*y2]) >= 6)
c3 = model.addConstr(quicksum([2*y1, 2*y2, 4*y3, 4*y4]) >= 15)
c4 = model.addConstr(quicksum([2*y1, 4*y2, y3, 5*y4]) >= 10)

model.update()
model.optimize()

print("=====================================\n\n Dual: \n\n")

model = Model()

# Set Variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = model.addVar(vtype=GRB.CONTINUOUS, name='x2')
x3 = model.addVar(vtype=GRB.CONTINUOUS, name='x3')
x4 = model.addVar(vtype=GRB.CONTINUOUS, name='x4')
    
model.update()
    
# Set objective
model.setObjective(quicksum([2000*x1, 6*x2, 15*x3, 10*x4]), GRB.MAXIMIZE)
model.update()

# Set constraints
c1 = model.addConstr(quicksum([400*x1, 3*x2, 2*x3, 2*x4]) <= 1.25)
c2 = model.addConstr(quicksum([200*x1, 2*x2, 2*x3, 4*x4]) <= 2)
c3 = model.addConstr(quicksum([150*x1      , 4*x3, 1*x4]) <= 1)
c4 = model.addConstr(quicksum([500*x1      , 4*x3, 5*x4]) <= 4)

model.update()
model.optimize()

