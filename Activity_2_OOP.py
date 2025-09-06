class Dog():
    def move(self):
        return "Walk"

class Cat:
    def move(self):
        return "Walk"
    
class Eagle:
    def move(self):
        return "Fly"
    
class Gold_fish:
    def move(self):
        return "Swim"
    
class Snail:
    def move(self):
        return "Crawl"
    
class Kangaroo:
    def move(self):
        return "Jump"

# Polymorphism in action
for animal in [Dog(), Cat(), Eagle(), Gold_fish(), Snail(), Kangaroo()]:
    print(animal.move())