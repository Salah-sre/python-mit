#switch/case statements
letters = {
    1: 'alpha',
    2: 'beta',
    3: 'gamma',
    4: 'delta'
}

print(letters.get(4, 'unknown'))

def conversion():
    num = int(input('Enter a number: ' ))
    base = input('Convert to [bin/oct/hex]: ')
    functions = dict(bin=bin, oct=oct, hex=hex)
    function = functions.get(base)
    if function is not None:
        print('The result is', function(num))
    else: 
        print('Invalid conversion')

conversion()
