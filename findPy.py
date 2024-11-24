import locale, math, numpy, os, random
import matplotlib.pyplot as plt

# Tell Python which local standard to use
if os.name in ('mac', 'posix'):
  locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') #MAC
else: 
  locale.setlocale(locale.LC_ALL, '') #PC 

#Format ints according to local standard
def formatInt(myint):
  return locale.format_string('%d', myint, grouping = True)

def throwDarts(numDarts, shouldPlot):
  inCircle = 0
  estimates = []
  for darts in range(1, numDarts + 1, 1):
#Generates a random float in [0-1[ range
    x = random.random()
    y = random.random()
    if math.sqrt(x*x + y*y) <= 1.0:
      inCircle += 1
    if shouldPlot:
      piGuess = 4*(inCircle/float(darts))
      estimates.append(piGuess)
    if darts%1000000 == 0:
      piGuess = 4*(inCircle/float(darts))
      dartsStr = locale.format_string('%d', darts, True)
      print('Estimate with ', formatInt(darts), 'darts: ', piGuess)
  if shouldPlot:
    xAxis = numpy.arange(1, len(estimates) + 1)
    plt.semilogx(xAxis, estimates)
    titleStr = 'Estimations of pi, final estimate: ' + str(piGuess)
    plt.title(titleStr)
    plt.xlabel('Number of Darts Thrown')
    plt.ylabel('Estimate of pi')
    plt.axhline(3.14159)
  return 4*(inCircle/float(numDarts))

def findPi(numDarts, shouldPlt = False):
  piGuess = throwDarts(numDarts, shouldPlt)
  print('Estimate value of Pi with ', formatInt(numDarts), 'darts: ', piGuess)

#findPi(10000, True)
findPi(10000000000)
plt.show()
