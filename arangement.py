class Arrangement:

    def __init__(self):
        self.flowers = list()

    def enhance(self, flower):
        self.flowers.append(flower)

    def __str__(self):
        return(f"{self.flowers}")

class MothersDay(Arrangement):

    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added
    def enhance(self, flower):
        try:
            if flower.organic == False:
                super().enhance(flower)
        except AttributeError:
            print("only organic flowers maybe added to the mother's day arrangement")

class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
    def enhance(self, flower):
        try:
            if flower.organic == True:
                super().enhance(flower)
        except AttributeError:
            print("only non organic flowers maybe added to the mother's day arrangement")

class Flower:
    def __str__(self):
        return("flower")

class Daisy(Flower):
    def __init__(self):
        self.organic = True

class Baby_Breath(Flower):
    def __init__(self):
        self.organic = True

class Poppy(Flower):
    def __init__(self):
        self.organic = True

class Rose(Flower):
    def __init__(self):
        self.organic = False
        self.color = ["red", "pink", "blue"]

class Lilly(Flower):
    def __init__(self):
        self.organic = False

class Alstroemeria(Flower):
    def __init__(self):
        self.organic = False

if __name__ == "__main__":
    for_beth = ValentinesDay()
    red_rose = Rose()

    for_beth.enhance(red_rose)

for_mom = MothersDay()
pop = Poppy()
baby = Baby_Breath()
daisy = Daisy()

for_mom.flowers.append(pop)
for_mom.enhance(baby)
for_mom.enhance(daisy)


print(for_mom)
print(for_beth)