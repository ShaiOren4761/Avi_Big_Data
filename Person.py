class Person:

    def __init__(self, name, tz):
        self.name = name
        self.tz = tz
        self.children = []

    def add_family(self, family):
        self.family = family

    def change_family(self, family):
        self.family = family
        self.add_family(family)

    def add_second_family(self, family):
        self.family += ' ' + family

    def add_children(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def print_children(self):
        print(f'{self.name} has {self.children.__len__()} children.')
        print(f"Children names: {[name for name in self.children]}")


p1 = Person('Danni', '001')
print(f'the first person is {p1.name}')

p2 = Person('Shani', 102)
print(f'the 2nd person is {p2.name}')

p2.add_family('kukit')
p1.add_family('kuki')

p2.add_second_family(p1.family)

c1 = Person('kiki', 110)
c2 = Person('keke', 210)

p1.add_children(c1)
p1.add_children(c2)

c3 = Person('titi', 810)
c4 = Person('tete', 710)
c5 = Person('baba', 669)

p2.add_children(c3)
p2.add_children(c4)
p2.add_children(c5)


print()

# Dani and Shani had 3 children
# Add an attribute children that prints the children person.children