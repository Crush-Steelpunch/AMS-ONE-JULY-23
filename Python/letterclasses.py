class lettertests:

    def __init__(self,inputstringofletter):
        self.stringofletter = inputstringofletter

    def testletter(self,inputletter):
        if inputletter.upper() in self.stringofletter:
            return "True"
        else:
            return "False"


horizsymm = lettertests('BCDEHIKOX')
vertsymm = lettertests('AHIMOTUVWXY')
horizvertsym = lettertests('HIOX')
rotsymm = lettertests('HINOSXZ')

userletter=''

while userletter != '0':
    userletter = input('enter a single charactor, 0 to quit: ')
    print("is Horiz Symm " + horizsymm.testletter(userletter))
    print("is VertSymm " + vertsymm.testletter(userletter))
    print("is h+vSymm " + horizvertsym.testletter(userletter))
    print("is rotSymm " + rotsymm.testletter(userletter))