class Dog:
    numlegs = 4
    numpaws = 4
    numtail = 1
    numears = 2
    canlayeggs = False
    canfly = False
    canbark = True
    
    def bark(self):
        print ("woof wood")
    def eat(self):
        print ("dog eats")
    def play(self):
        print ("dog plays with ball")

french_bulldog = Dog()
golden_retreaver = Dog()

print(french_bulldog.numears, french_bulldog.canlayeggs, french_bulldog. numpaws)
print(golden_retreaver.numlegs, golden_retreaver.numears, golden_retreaver.canlayeggs, golden_retreaver.canfly)

french_bulldog.bark()
french_bulldog.eat()
golden_retreaver.play()
