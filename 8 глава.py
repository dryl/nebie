class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("Я нашел еду!")
        self.eat_food()
    def eat_leaves_from_trees(self):
        print('ест листья')
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots
    
reginald = Giraffes(100)
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)
#reginald.dance_a_jig()
#reginald.move()
#reginald.breathe()
#reginald.eat_food()
#reginald.feed_young_with_milk()
#reginald.eat_leaves_from_trees()
harold = Giraffes(150)
#harold.move()
