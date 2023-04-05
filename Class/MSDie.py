import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides
    """    

    def __init__(self, num_sides) -> None:
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)
    
    def __eq__(self,other):
        return self.current_value == other.current_value
    
    def __lt__(self,other):
        return self.current_value < other.current_value
    

####### Test

if __name__=="__main__":
    my_die1 = MSDie(6)
    my_die2 = MSDie(6)
    for i in range(5):
        print(my_die1, my_die2)
        print(my_die1==my_die2)
        print(my_die1 < my_die2)
        my_die1.roll()
        my_die2.roll()

    d_list = [MSDie(6), MSDie(20)]
    print(d_list)


