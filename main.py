from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Hospital_Resource_Allocation", LpMaximize)

x1 = LpVariable("Critical_Patients", lowBound=0)
x2 = LpVariable("Serious_Patients", lowBound=0)
x3 = LpVariable("Mild_Patients", lowBound=0)

model += 10*x1 + 6*x2 + 2*x3

model += x1 + x2 + x3 <= 100
model += x1 + 0.5*x2 <= 40

model.solve()

print("Critical Patients:", x1.value())
print("Serious Patients:", x2.value())
print("Mild Patients:", x3.value())
print("Max Score:", model.objective.value())