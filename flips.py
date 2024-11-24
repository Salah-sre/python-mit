import math, random, numpy
import matplotlib.pyplot as plt

def flipTrial(numFlips):
  heads, tails = 0, 0
  for i in range(0, numFlips):
    coin = random.randint(0, 1)
    if coin == 0: heads += 1
    else: tails += 1
  return heads, tails

def simFlips(numFlips, numTrials):
  diffs = []
  for i in range(0, numTrials):
    heads, tails = flipTrial(numFlips)
    diffs.append(abs(heads - tails))

# statistics
  diffs = numpy.array(diffs)
  diffMean = sum(diffs)/len(diffs)
# Normalize
  diffPercent = (diffs/float(numFlips))*100
  percentMean = sum(diffPercent)/len(diffPercent)

  plt.hist(diffs)
  plt.axvline(diffMean, label = 'Mean')
  plt.legend()
  titleString = str(numFlips) + ' Flips: ' + str(numTrials) + ' Trials'
  plt.title(titleString)
  plt.xlabel('Diff between heads and tails')
  plt.ylabel('Num of trials')
  plt.figure()

  plt.plot(diffPercent)
  plt.axhline(percentMean, label = 'Mean')
  plt.legend()
  plt.title(titleString)
  plt.xlabel('Trial Number')
  plt.ylabel('Percent Diff between heads and tails')

simFlips(100, 100)

#plt.figure()

plt.show()

