import numpy as np
from gurobipy import *


def main():
    mod = Model("guchi")
    x1 = mod.addVar(vtype=GRB.INTEGER, name='purse')
    x2 = mod.addVar(vtype=GRB.INTEGER, name='bag')
    x3 = mod.addVar(vtype=GRB.INTEGER, name='backpack')
    mod.update()

    mod.setObjective(24*x1 + 22*x2 + 45*x3, GRB.MAXIMIZE)

    mod.addConstr(2*x1 + x2 + 3*x3 <= 42, name='leather')
    mod.addConstr(6*x1 + x2 + 2*x3 <= 40, name='sewing')
    mod.addConstr(x1 + 0.5*x2 + x3 <= 45, name='finishing')

    mod.optimize()
    
    print('')
    print('optimal solution')
    sol = mod.getVars()
    for s in sol:
        print(s.varName, s.x)
        
    print('')
    print('optimal objective value  = ', mod.objVal)
    
    print('')
    for c in mod.getConstrs():
        print(c.constrName, c.slack)

if __name__ == '__main__':
    main()