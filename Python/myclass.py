class Dog:

#    colour = ""
#    breed = ""
#    personality = ""
#    barkstr = ""

    def __init__(inputcolour,inputbreed,inputpersonality,inputbarkstr):
        self.colour = inputcolour
        self.breed = inputbreed
        self.personality = inputpersonality
        self.barkstr = inputbarkstr

    def bark(self):
        return self.barkstr

    def runabout():
        pass

    def playgames():
        pass

fluffy = Dog("Yellow and Brown","Lab","Relaxed","Woof")

bob = Dog("Gold","Sausagedog","depressed","yipyipyip"
)
Spot = Dog("Green","Animedog","bubbly","Whazzup")

print(Spot.bark(),bob.bark(),fluffy.bark())

breakpoint()
