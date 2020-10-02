class Animal:
    _zoo_name = "Hayaton"

    def __init__(self, _name=None, _hunger=None):
        self._name = _name
        self._hunger = _hunger

    def size(self):
        if isinstance(self._name, int):
            return self._name
        else:
            return len(self._name)

    def get_name(self):
        return self._name

    def get_zoo_name(self):
        return self._zoo_name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        print("talk")

    def size(self):
        super().size()
        if 15 < self.weight <= 20:
            return "Fat"
        elif self.weight > 20:
            return "Very Fat"
        else:
            return "OK"


class Cat(Animal):
    def __init__(self, _name, _hunger):
        Animal.__init__(self, _name, _hunger)

    def talk(self):
        print("Meow")

    def chase_lazer(self):
        print("Meeeeoooow")


class Dog(Animal):
    def __init__(self, _name, _hunger):
        Animal.__init__(self, _name, _hunger)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("there you go, sir!")


class Skunk(Animal):
    def __init__(self, _name, _hunger, _stink_count=6):
        Animal.__init__(self, _name, _hunger)

    def talk(self):
        print("tssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    def __init__(self, _name, _hunger):
        Animal.__init__(self, _name, _hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("im not your toy..")


class Dragon(Animal):
    def __init__(self, _name, _hunger, _color="Green"):
        Animal.__init__(self, _name, _hunger, _zoo_name)

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$@#$")


def main():
    zoo_list = []
    B = Dog("Brownie", 10)
    zoo_list.append(B)
    Z = Cat("Zelda", 3)
    zoo_list.append(Z)
    S = Skunk("Stinky", 0)
    zoo_list.append(S)
    K = Unicorn("Keith", 7)
    zoo_list.append(K)
    L = Dragon("Lizzy", 1450)
    zoo_list.append(L)
    m = Dragon("McFly", 80)
    zoo_list.append(m)
    d = Dog("Doggo", 80)
    zoo_list.append(d)
    k = Cat("Kitty", 3)
    zoo_list.append(k)
    s = Skunk("Stinky Jr.", 80)
    zoo_list.append(s)
    c = Unicorn("Clair", 80)
    zoo_list.append(c)

    for animal in zoo_list:
        print(type(animal).__name__, animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        if isinstance(animal, Cat):
            animal.chase_lazer()
        if isinstance(animal, Skunk):
            animal.stink()
        if isinstance(animal, Unicorn):
            animal.sing()
        if isinstance(animal, Dragon):
            animal.breath_fire()

    print(super.animal.get_zoo_name())


main()
