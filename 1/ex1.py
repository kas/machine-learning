import csv
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

with open('ex1/ex1data1.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))

plt.scatter(x, y, marker='x')
plt.xlabel('Profit in $10,000s')
plt.ylabel('Population of City in 10,000s')
plt.show()
