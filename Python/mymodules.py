def fourcandles(numberofcandles=4):
    candlelist = []
    for i in range(numberofcandles):
        candlelist.append('candle')
    return candlelist

def mrshouty(stringtomakeshouty):
    return stringtomakeshouty.upper()

def add5toanynumber(goingtoadd5:float):
    return goingtoadd5+5

def aceififyer(makemoreace):
    return f"{makemoreace} is ace"

#def len():
#    return "Hi, I am Len"


def nameofthefunction(parameter1):
    parameter1 = parameter1 + "sometext"
    return "This is Data out of a function with: " + parameter1


def testifprime(numin):
    if numin%2 != 0:
        return True
    else:
        return False
    
def ifstatementfunction(strinvar):
    if strinvar == "pies":
        return True
    elif 'o' in strinvar:
        return True
    elif len(strinvar) > 15:
        return True
    else:
        return False
