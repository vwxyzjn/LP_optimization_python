# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 13:02:31 2017

@author: costa

Simple Primal Dual Example.
"""


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
y5 = model.addVar(vtype=GRB.CONTINUOUS, name='y5')
y6 = model.addVar(vtype=GRB.CONTINUOUS, name='y6')
y7 = model.addVar(vtype=GRB.CONTINUOUS, name='y7')
    
model.update()
    
# Set objective
model.setObjective(quicksum([y1,y2,y3,y4,y5,y6,y7]), GRB.MAXIMIZE)
model.update()

# Set constraints
model.addConstr(quicksum([y1,y3]) <= 1)
model.addConstr(quicksum([y1,y2,y3]) <= 1)
model.addConstr(quicksum([y2,y5]) <= 1)
model.addConstr(quicksum([y3,y6]) <= 1)
model.addConstr(quicksum([y4,y6,y7]) <= 1)
model.addConstr(quicksum([y5,y7]) <= 1)

model.update()
model.optimize()

print("=====================================\n\n Dual: \n\n")

model = Model()

# Set Variables
x11 = model.addVar(vtype=GRB.CONTINUOUS, name='x11')
x12 = model.addVar(vtype=GRB.CONTINUOUS, name='x12')
x13 = model.addVar(vtype=GRB.CONTINUOUS, name='x13')
x21 = model.addVar(vtype=GRB.CONTINUOUS, name='x21')
x22 = model.addVar(vtype=GRB.CONTINUOUS, name='x22')
x23 = model.addVar(vtype=GRB.CONTINUOUS, name='x23')
    
model.update()
    
# Set objective
model.setObjective(quicksum([x11,x12,x13,x21,x22,x23]), GRB.MINIMIZE)
model.update()

# Set constraints
model.addConstr(quicksum([x11,x12]) >= 1)
model.addConstr(quicksum([x12,x13]) >= 1)
model.addConstr(quicksum([x11,x21]) >= 1)
model.addConstr(quicksum([x12,x22]) >= 1)
model.addConstr(quicksum([x13,x23]) >= 1)
model.addConstr(quicksum([x21,x22]) >= 1)
model.addConstr(quicksum([x22,x23]) >= 1)

model.update()
model.optimize()
