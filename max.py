# Exponential growth / complexity

def maxVal(w, v, i, availableWeight):
  print('maxVal called with:', i, availableWeight)
  global numCalls
  numCalls += 1

  if i == 0:
    if w[i] <= availableWeight: return v[i]
    else: return 0
    
# left branch in decision tree
  without_i = maxVal(w, v, i-1, availableWeight)
  if w[i] > availableWeight:
      return without_i

# right branch
  else:
    with_i = v[i] + maxVal(w, v, i-1, availableWeight - w[i])
  
  return max(with_i, without_i)

# Dynamic programming by using mem to store calculations
def fastMaxVal(w, v, i, aW, mem):
  global numCalls
  numCalls += 1

  try: return mem[(i, aW)]
  except KeyError:
    if i == 0:
      if w[i] <= aW:
        mem[(i, aW)] = v[i] 
        return v[i]
      else: 
        mem[(i, aW)] = 0
        return 0
     
    without_i = fastMaxVal(w, v, i-1, aW, mem)
    if w[i] > aW:
      mem[(i, aW)] = without_i
      return without_i
    else:
      with_i = v[i] + fastMaxVal(w, v, i-1, aW - w[i], mem)
    
    result = max(with_i, without_i)
    mem[(i, aW)] = result
    return result

def fastMaxValCall(w, v, i, aW):
  mem = {} 
  return fastMaxVal(w, v, i, aW, mem)

#weights = [1, 5, 3, 4]
#vals = [15, 10, 9, 5]
#numCalls = 0
#res = maxVal(weights, vals, len(vals) - 1, 8)
#print('max val = ', res, 'number of calls = ', numCalls)

w = [5, 5, 1, 8, 2, 9, 7, 5, 2, 8, 1, 2, 7, 3]
v = [5, 5, 3, 5, 8, 6, 7, 2, 3, 7, 1, 8, 3, 6]
numCalls = 0
res = maxVal(w, v, len(v) - 1, 30)
print('max val = ', res, 'number of calls = ', numCalls)

w = [5, 5, 1, 8, 2, 9, 7, 5, 2, 8, 1, 2, 7, 3]
v = [5, 5, 3, 5, 8, 6, 7, 2, 3, 7, 1, 8, 3, 6]
numCalls = 0
res = fastMaxValCall(w, v, len(v) - 1, 30)
print('max val = ', res, 'number of calls = ', numCalls)

