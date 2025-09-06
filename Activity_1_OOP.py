class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

cat1 = Cat("Mittens", "Black and white")
cat2 = Cat("Caramel", "Ginger")
cat3 = Cat("Shadow", "Gray")
cat4 = Cat("Luna", "Calico")
cat5 = Cat("Simba", "Orange tabby")

class Cat:
    def __init__(self, breed):
        self.breed1 = "Calico"
        self.breed2 = "Lion"

class SmallCat(Cat):
    pass
SmallCat = SmallCat("Calico")

class BigCat(Cat):
    pass
BigCat = BigCat("Lion")

print(SmallCat.breed1)
print(BigCat.breed2)