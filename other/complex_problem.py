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
r = model.addVar(vtype=GRB.CONTINUOUS, name='r')
t = model.addVar(vtype=GRB.CONTINUOUS, name='t')
a1 = model.addVar(vtype=GRB.CONTINUOUS, name='a1')
a2 = model.addVar(vtype=GRB.CONTINUOUS, name='a2')
array = [x1,x2,r,t,a1,a2]

model.update()

# Set objective
model.setObjective(
    quicksum([15*x1, 8*x2, -1.5*r, -6*t, -1*a1, -1*a2]),
    GRB.MAXIMIZE
)
model.update()

# Set constraints
model.addConstr(0.75*x1 + 0.5*x2 <= 160 + t)
model.addConstr(1.5*x1 + 0.8*x2 <= 320)
model.addConstr(2*x1 + x2 <= r)
model.addConstr(r <= 400)
model.addConstr(x1 <= 50 + 10*a1)
model.addConstr(x2 <= 60 + 15*a2)

model.update()
model.optimize()
print(array)

print(""" \n\n (a) part of the problem DUAL \n\n""")

model = Model()
l = model.addVar(vtype=GRB.CONTINUOUS, name='l')
m = model.addVar(vtype=GRB.CONTINUOUS, name='m')
rp = model.addVar(vtype=GRB.CONTINUOUS, name='rp')
d1 = model.addVar(vtype=GRB.CONTINUOUS, name='d1')
d2 = model.addVar(vtype=GRB.CONTINUOUS, name='d2')
r = model.addVar(vtype=GRB.CONTINUOUS, name='r')
array = [l,m,rp,d1,d2,r]

model.update()

# Set objective
model.setObjective(
    quicksum([160*l, 320*m, 50*d1, 60*d2, 400*r]),
    GRB.MINIMIZE
)

model.update()

# Set constraints

model.addConstr(0.75*l + 1.5*m + 2*rp + 1*d1 >= 15)
model.addConstr(0.5*l + 0.8*m + 1*rp + 1*d2 >= 8)
model.addConstr(-1*rp + 1*r >= -1.5)
model.addConstr(-1*l >= -6)
model.addConstr(-10*d1 >= -1)
model.addConstr(-15*d2 >= -1)

model.update()
model.optimize()
print(array)



print(""" Experiment with the problem \n\n""")

model = Model()

# Set Variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = model.addVar(vtype=GRB.CONTINUOUS, name='x2')
r = model.addVar(vtype=GRB.CONTINUOUS, name='r')
t = model.addVar(vtype=GRB.CONTINUOUS, name='t')
a1 = model.addVar(vtype=GRB.CONTINUOUS, name='a1')
a2 = model.addVar(vtype=GRB.CONTINUOUS, name='a2')
array = [x1,x2,r,t,a1,a2]

model.update()

# Set objective
model.setObjective(
    quicksum([15*x1, 8*x2, -1.5*r, -2*t, -1*a1, -1*a2]),
    GRB.MAXIMIZE
)
model.update()

# Set constraints
model.addConstr(0.75*x1 + 0.5*x2 <= 160 + t)
model.addConstr(1.5*x1 + 0.8*x2 <= 320)
model.addConstr(2*x1 + x2 <= r)
model.addConstr(r <= 400)
model.addConstr(x1 <= 50 + 10*a1)
model.addConstr(x2 <= 60 + 15*a2)

model.update()
model.optimize()
print(array)
