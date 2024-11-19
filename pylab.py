import random
import matplotlib.pyplot as plt
import numpy

plt.plot([1, 2, 3, 4])
plt.plot([5, 6, 7, 8])
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.figure()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.title('Earnings')
plt.xlabel('Days')
plt.ylabel('Dollars')

plt.figure()
xAxis = numpy.array([1, 2, 3, 4])
print(xAxis)
test = numpy.arange(1, 5)
print(test)
print(test == xAxis)
yAxis = xAxis**3
plt.plot(xAxis, yAxis, 'ro')

plt.figure()
vals = []
dieVals = numpy.arange(1, 7)
for i in range(10000):
  vals.append(random.choice(dieVals) + random.choice(dieVals))
plt.hist(vals, bins=11)
plt.show()
