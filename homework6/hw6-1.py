class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        if self.species == 'Cow':
            print('MOOO')
        elif self.species == 'Cat':
            print('MEOW')
        else:
            print('Species sound not found')

cow = Animal('Korova', 'Cow', 10)
cat = Animal('Murzyk', 'Cat', 8)
cow.make_sound()
cat.make_sound()
