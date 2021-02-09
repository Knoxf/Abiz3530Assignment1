"""
Description: - This script will find the least cost logistics as determined by linear programming.

Requirements:

- Python 3
- PuLP library

@author: Nick Kuznetsov
"""

from pulp import *

Sheds = ["A", "B", "C"]
supply = {"A": 600,
          "B": 300,
          "C": 300}
Barns = ["1", "2", "3", "4", "5", "6", "7"]
demand = {"1": 150,
          "2": 250,
          "3": 200,
          "4": 250,
          "5": 200,
          "6": 150,
          "7": 200}
costs = [
    [1.6, 1.8, 1.1, 1.5, 1.7, 1.0, 1.5],
    [1.4, 1.2, 1.3, 1.1, .9, .8, .9],
    [1.3, 1.5, 1.7, 1.8, 1.9, 2.0, 1.7]
]
costs = makeDict([Sheds, Barns], costs, 0)
prob = LpProblem("ch2optlogistics", LpMinimize)
Routes = [(s, b) for s in Sheds for b in Barns]
vars = LpVariable.dicts("Route", (Sheds, Barns), 0, None, LpInteger)
prob += lpSum([vars[s][b] * costs[s][b] for (s, b) in Routes]), "Trans_Costs"
for s in Sheds:
    prob += lpSum([vars[s][b] for b in Barns]) <= supply[s], "From_Shed_%s" % s
for b in Barns:
    prob += lpSum([vars[s][b] for s in Sheds]) >= demand[b], "To_Barn%s" % b
prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)
print("Cost_of_Transportation = ", value(prob.objective))
