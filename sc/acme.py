from random import randint

class Product:

    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    def stealability(self):
        '''calculates the price divided by the weight
        '''
        steal_ratio = (self.price / self.weight)
        
        if steal_ratio >= 0.5:
            print('Kinda stealable')
        elif steal_ratio < 0.5:
            print('Not so stealable...')
        else:
            print('Very stealable!')
    
    def explode(self):
        '''calculates the flammability times the weight
        '''
        flames = self.flammability * self.weight

        if flames < 10.0:
            print('...fizzle')
        elif flames >= 50.0:
            print('...BABOOM!')
        else:
            print("...boom!")

class BoxingGlove(Product):

    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)
    
    def explode(self):
        '''calculates the flammability times the weight
        '''
        print("...it's a glove") 
    
    def punch(self):

        if self.weight < 5:
            print('That tickles')
        if self.weight > 15:
            print('OUCH!')
        else:
            print('Hey that hurts!')
    

