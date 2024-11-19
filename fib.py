
def fib(n):
  global numCalls
  numCalls += 1
  print('Fib called with', n)
  if n <= 1:
    return n
  else:
    return fib(n-1) + fib(n-2)

def fastFib(n, memo):
  global numCalls
  numCalls += 1
  print('Fib called with', n) 
  if not n in memo:
    memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)  
  return memo[n]

def callFastFib(n):
  memo = {0:0, 1:1}
  return fastFib(n, memo)
 
#numCalls = 0
#n = 6
#res = fib(n)
#print('Fib of', n, 'is', res, 'numCalls =', numCalls)

numCalls = 0
n = 6
res = callFastFib(n)
print('Fib of', n, 'is', res, 'numCalls =', numCalls)
