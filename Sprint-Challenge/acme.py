import random


class Product():
    """
    Class used to  organize the vast quantities
    and variety of goods the acme company manages
    and sells.
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """
         calculates the price divided by the weight,
         returns a message based on calculated ratio
        """
        stealable = self.price / self.weight

        if stealable < 0.5:
            return "Not so stealable..."
        elif stealable >= 0.5 and stealable < 1:
            return "Kinda stealable..."
        else:
            return "Very Stealable!"

    def explode(self):
        """
        calculates the flammability times the weight,
        returns a message indicating its explosiveness
        """
        explosive = self.flammability * self.weight

        if explosive < 10:
            return "...fizzle"
        elif explosive >= 10 and explosive < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        super().__init__(name, price, weight,
                         flammability, identifier)

    def explode(self):
        # overide explode because..
        return "...it's a glove"
        # and gloves don't explode

    def punch(self):
        """
        Returns a message indicating pain delivered
        based on Product weight
        """
        pain = self.weight

        if pain < 5:
            return "That tickles."
        elif pain >= 5 and pain < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
