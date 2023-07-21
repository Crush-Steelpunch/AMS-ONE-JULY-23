import mymodules

def test_firsttest():
    assert mymodules.add5toanynumber(5)  == 10
    assert mymodules.add5toanynumber(0)  == 5
    assert mymodules.add5toanynumber(5)  != 5

def test_shoutytest():
    assert mymodules.mrshouty('b') == 'B'
    assert mymodules.mrshouty('0') == '0'
    assert mymodules.mrshouty('abcABC') == 'ABCABC'

def test_ace():
    assert mymodules.aceififyer('Mr Peas') == 'Mr Peas is ace'

def test_isprime():
    assert mymodules.testifprime(5) == True
    assert mymodules.testifprime(4) == False
    assert mymodules.testifprime(1) == True
#    assert mymodules.testifprime(15) == False
#    assert mymodules.testifprime(2) == True


def test_strinintest():
    assert mymodules.ifstatementfunction('pies') == True
    assert mymodules.ifstatementfunction('This has vowels') == True
    assert mymodules.ifstatementfunction('mvre than 15 charactvrs') == True
    assert mymodules.ifstatementfunction('') == False