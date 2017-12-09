from gurobipy import Model, GRB

print("=====================================\n\n Primal: \n\n")

model = Model()

# Set Variables
x1 = model.addVar(vtype=GRB.CONTINUOUS, name='x1')
x2 = model.addVar(vtype=GRB.CONTINUOUS, name='x2')
x3 = model.addVar(vtype=GRB.CONTINUOUS, name='x3')
z = model.addVar(vtype=GRB.CONTINUOUS, name='z', lb=-1e20) ## VERY IMPORTANT !!!!!, lb=-1e20 means
                                                           ## the variable is unrestricted. lb stands for 
                                                           ## lowerbound. The default lb is 0.
    
model.update()
    
# Set objective
model.setObjective(z, GRB.MINIMIZE)
model.update()

# Set constraints
c1 = model.addConstr(x1+x2+x3 == 1)
c2 = model.addConstr(z + (-2)*x1 + x2 >= 0)
c3 = model.addConstr(z + 3*x1 + (-1)*x2 + (-1)*x3 >= 0)

model.update()
model.optimize()
print('\n\n', [x1,x2,x3, z])


print("=====================================\n\n Dual: \n\n")
model = None
model = Model()

# Set Variables
y1 = model.addVar(vtype=GRB.CONTINUOUS, name='y1')
y2 = model.addVar(vtype=GRB.CONTINUOUS, name='y2')
z_p = model.addVar(vtype=GRB.CONTINUOUS, name='z_p', lb=-1e20)

model.update()
    
# Set objective
model.setObjective(z_p, GRB.MAXIMIZE)
model.update()

# Set constraints
c1 = model.addConstr(y1 + y2 == 1)
c2 = model.addConstr(z_p + (-2)*y1 + 3*y2 <= 0)
c3 = model.addConstr(z_p + y1 + (-1)*y2 <= 0)
c4 = model.addConstr(z_p + (-1)*y2 <= 0)

model.update()
model.optimize()

print('\n\n', [y1,y2,z_p])