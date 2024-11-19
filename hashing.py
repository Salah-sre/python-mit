def create(smallest, largest):
  intSet = []
  for i in range(smallest, largest + 1): intSet.append(None)
  return intSet

def insert(intSet, e):
  intSet[e] = 1

def member(intSet, e):
  return intSet[e] == 1

def hashChar(c):
  return ord(c)

def cSetCreate():
  cSet = []
  for i in range(0, 255): cSet.append(None)
  return cSet

def cSetInsert(cSet, e):
  cSet[hashChar(e)] = 1

def cSetMember(cSet, e):
  return cSet[hashChar(e)] == 1

