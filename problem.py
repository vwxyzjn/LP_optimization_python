# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:28:01 2017

@author: shuang
"""
from gurobipy import *
import pandas

i_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
j_set = ['1s1', '2s1','3m1','4m1','5t1','6t1','5t2','6t2','5t3','6t3','7w1','8w1','7w2','8w2', '5b', '6b', '7b', '8b']

model = Model()

# Set Variables
x = {}
for i in i_set:
    for j in j_set:
        x[str(i)+'~'+j] = model.addVar(vtype=GRB.BINARY, name=str(i) + '~' + j)
        
model.update()

# Set objective
model.setObjective(quicksum(x[key] for key in x.keys()), GRB.MINIMIZE)

# Add constraints
c = {}

# 1. meet the conference demands
conference_demands = [2,2,2,2,2,2,1,1,1,1,2,2,1,1]
c_i = 0  # conference index
conference_shift = j_set[:-4] # without '5b'...
for j in conference_shift:
    c['x_i~' + j] = model.addConstr(quicksum(x[str(i)+'~' + j] for i in i_set) >= conference_demands[c_i], name='x_i~' + j + ' >= ' + str(conference_demands[c_i]))
    c_i += 1

# 2. meet the volunteers availability
availability = pandas.read_excel('Availability.xlsx').transpose()
for i in i_set:
    for j in j_set:
        c[str(i)+'~'+j +" <= A_" + str(i) + '~' + j] = model.addConstr(x[str(i)+'~'+j] <= availability.loc[i, j], name=str(i)+'~'+j +" <= A_" + str(i) + '~' + j)


# 3. special constraints
# 3.1 student 2 and student 5
c["x_2~j <= 1"] = model.addConstr(quicksum(x['2~' + j] for j in j_set) <= 1, name="x_2~j <= 1")
c["x_5~j <= 1"] = model.addConstr(quicksum(x['5~' + j] for j in j_set) <= 1, name="x_5~j <= 1")

# 3.2 
c["x_i~5b >= 1"] = model.addConstr(quicksum(x[str(i)+'~5b'] for i in i_set) >= 1, name="x_i~5b >= 1")
c["x_i~6b >= 1"] = model.addConstr(quicksum(x[str(i)+'~6b'] for i in i_set) >= 1, name="x_i~6b >= 1")
c["x_i~7b >= 1"] = model.addConstr(quicksum(x[str(i)+'~7b'] for i in i_set) >= 1, name="x_i~7b >= 1")
c["x_i~8b >= 1"] = model.addConstr(quicksum(x[str(i)+'~8b'] for i in i_set) >= 1, name="x_i~8b >= 1")

# 4. no students can be assigned to different location during the same shift
for i in i_set:
    all_location = ['5t1', '5t2', '5t3', '5b']
    c["x_" + str(i) + "~5(k) <= 1"] = model.addConstr(quicksum(x[str(i)+'~' + k] for k in all_location) <= 1, name="x_" + str(i) + "~5(k) <= 1")
    all_location = ['6t1', '6t2', '6t3', '6b']
    c["x_" + str(i) + "~6(k) <= 1"] = model.addConstr(quicksum(x[str(i)+'~' + k] for k in all_location) <= 1, name="x_" + str(i) + "~6(k) <= 1")
    all_location = ['7w1', '7w2', '7b']
    c["x_" + str(i) + "~7(k) <= 1"] = model.addConstr(quicksum(x[str(i)+'~' + k] for k in all_location) <= 1, name="x_" + str(i) + "~7(k) <= 1")
    all_location = ['8w1', '8w2', '8b']
    c["x_" + str(i) + "~8(k) <= 1"] = model.addConstr(quicksum(x[str(i)+'~' + k] for k in all_location) <= 1, name="x_" + str(i) + "~8(k) <= 1")


model.update()