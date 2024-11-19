def readFloat(reqMsg, errorMsg):
  while True:
    val = input(reqMsg)
    try:
      val = float(val)
      return val
    except:
      print(errorMsg)

print(readFloat('Enter float:', 'Not a float'))

