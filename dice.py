import random, numpy
import matplotlib.pyplot as plt

fair = [1, 2, 3, 4, 5, 6]

def throwPair(vals1, vals2):
  d1 = random.choice(vals1)
  d2 = random.choice(vals2)
  return d1, d2

def conductTrials(numThrows, die1, die2):
  throws = []
  for i in range(numThrows):
    d1, d2 = throwPair(die1, die2)
    throws.append(d1+d2)
  return throws

numThrows = 100000

throws = conductTrials(numThrows, fair, fair)
plt.hist(throws, 11)
plt.xticks(range(2, 13), ['2','3','4','5','6','7','8','9','10','11','12'])
plt.title('Distribution of values')
plt.xlabel('Sum of two die')
plt.ylabel('Number of throws')

#Get probabilities for fair dice
plt.figure()
sums = numpy.array([0]*14)
for val in range(2, 13):
  sums[val] = throws.count(val)
probs = sums[2:13]/float(numThrows)
xVals = numpy.arange(2, 13)
plt.plot(xVals, probs, label='Fair Dice')
plt.xticks(range(2, 13), ['2','3','4','5','6','7','8','9','10','11','12'])
plt.title('Probability of a value')
plt.xlabel('Sum of two die')
plt.ylabel('Probability')

plt.show()
