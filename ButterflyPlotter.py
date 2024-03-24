import sys
import csv
import numpy as np
import matplotlib.pyplot as plt


filename = ""
x = 0

if(len(sys.argv) != 2):
	filename = input("Enter filename: ")
else:
	filename = sys.argv[1]
	
data = list(csv.reader(open(filename)))
headings = data[0]
data = data[1:]
for i in range(len(data)):
	for j in range(len(data[0])):
		data[i][j] = float(data[i][j])
data = np.array(data)

data = np.transpose(data)
print(data[8])
print(data[9])
x = len(data) // 4
numPoints = len(data[0])
print(x)


colors = [np.random.rand(3)]* x
for i in range(x):
	color = (np.random.rand(3))
	colors[i] = color


for i in range(1):
	plt.plot(
		data[2* i + 1], 
		data[2*x + 2*i + 1],
		color=colors[i],
		label=headings[2*i + 1]
	)
	
for i in range(1):
	plt.plot(
		data[2*x + 2*i + 1], 
		data[2*i + 1],
		color=colors[i],
	)
	
x1 = [data[9][51-10-1], data[1][10]]
y1 = [data[1][51-10-1], data[1][51-10-1]]
plt.plot(x1, y1, 'r--', color = np.random.rand(3))
	
plt.legend()
plt.show()