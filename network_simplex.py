# -*- coding: utf-8 -*-
"""
Network simplex algorithm. 

three supply node with supply 20, 30, 40
four demand node with deman 15, 35, 20, 20

Cost from supply i to demand j is

   1   2  3  4
1  4   3  6  5
2  7  10  5  6
3  8   9  7  7
"""



from gurobipy import *
import pandas as pd

print("=====================================\n\n Primal: \n\n")
model = Model()

# Set up the cost matrix

C = pd.DataFrame(data= {1:[4,7,8], 2:[3,10,9], 3:[6,5,7], 4:[5,6,7]}, index=[1,2,3])

# Set Variables
X = pd.DataFrame(columns=[1,2,3,4], index=[1,2,3])
for i in range(1, len(X)+1):
    for j in range(1, len(X.loc[1])+1):
        X.loc[i,j] = model.addVar(vtype=GRB.CONTINUOUS, name=str(i)+'~'+str(j))

model.update()
    
# Set objective
r = range(1,4)
r2 = range(1,5)

model.setObjective(quicksum(C.loc[i,j]*X.loc[i,j]  for i in r for j in r2), GRB.MINIMIZE)
model.update()
#
## Set constraints
supply = pd.Series(data=[20,30,40], index=[1,2,3])
demand = pd.Series(data=[15,35,20,20], index=[1,2,3,4])
for i in r:
    model.addConstr(quicksum(X.loc[i,j] for j in r2) <= supply.loc[i])
for j in r2:
    model.addConstr(quicksum(X.loc[i,j] for i in r) >= demand.loc[j])


#
model.update()
model.optimize()
