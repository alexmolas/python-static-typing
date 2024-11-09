from abc import ABC, abstractmethod
import random


class Animal(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self._energy: int = 100

    @abstractmethod
    def make_sound(self) -> str:
        """Each animal must implement its own sound"""
        pass

    def eat(self, food_amount: int) -> None:
        """Increase energy when eating"""
        self._energy = min(100, self._energy + food_amount)

    @property
    def energy(self) -> int:
        """Read-only energy level"""
        return self._energy


class Mammal(Animal):
    """Class representing mammals with additional mammal-specific properties"""

    def __init__(self, name: str, age: int, fur_color: str) -> None:
        super().__init__(name, age)
        self.fur_color: str = fur_color
        self.body_temperature: float = 37.0

    def give_birth(self) -> None:
        """Mammals give birth to live young"""
        self._energy -= 50
        print(f"{self.name} gave birth!")


class Bird(Animal):
    """Class representing birds with flying capabilities"""

    def __init__(self, name: str, age: int, wingspan: float) -> None:
        super().__init__(name, age)
        self.wingspan: float = wingspan
        self.can_fly: bool = True

    def fly(self, distance: float) -> bool:
        """Birds can fly if they have enough energy"""
        energy_cost: int = int(distance * 0.1)
        if self._energy >= energy_cost:
            self._energy -= energy_cost
            print(f"{self.name} flew {distance} meters!")
            return True
        return False


class Cat(Mammal):
    """Specific implementation of a cat"""

    def __init__(
        self, name: str, age: int, fur_color: str, indoor: bool = True
    ) -> None:
        super().__init__(name, age, fur_color)
        self.indoor: bool = indoor

    def make_sound(self) -> str:
        """Cats meow!"""
        self._energy -= 1
        return "Meow!"

    def purr(self) -> None:
        """Cats can purr when happy"""
        print(f"{self.name} is purring...")


class Parrot(Bird):
    """Specific implementation of a parrot with speaking abilities"""

    def __init__(self, name: str, age: int, wingspan: float) -> None:
        super().__init__(name, age, wingspan)
        self.vocabulary: list[str] = []

    def make_sound(self) -> str:
        """Parrots squawk!"""
        self._energy -= 1
        return "Squawk!"

    def learn_word(self, word: str) -> None:
        """Parrots can learn new words"""
        self.vocabulary.append(word.lower())

    def speak(self) -> str | None:
        """Parrots can speak learned words if they have energy"""
        if self.vocabulary and self._energy >= 5:
            self._energy -= 5
            return f"{self.name} says: {random.choice(self.vocabulary)}"
        return None


def demonstrate_animal_behavior(animals: list[Animal]) -> dict[str, int]:
    """
    Function demonstrating polymorphism and type hints with a collection of animals
    Returns a dictionary with the energy levels of each animal
    """
    energy_levels: dict[str, int] = {}

    for animal in animals:
        print(f"\nDemonstrating {animal.__class__.__name__}: {animal.name}")
        print(f"Sound: {animal.make_sound()}")

        if isinstance(animal, Mammal):
            print(f"Fur color: {animal.fur_color}")

        if isinstance(animal, Bird):
            print(f"Wingspan: {animal.wingspan}m")
            animal.fly(10.0)

        if isinstance(animal, Parrot):
            animal.learn_word("Hello")
            print(animal.speak())

        if isinstance(animal, Cat):
            animal.purr()

        energy_levels[animal.name] = animal.energy

    return energy_levels


# Creating instances of different animals
kitty = Cat("Whiskers", 3, "orange")
polly = Parrot("Polly", 2, 0.3)

# Demonstrate inheritance and polymorphism
animals = [kitty, polly]
energy_report = demonstrate_animal_behavior(animals)

print("\nEnergy levels after demonstration:")
for name, energy in energy_report.items():
    print(f"{name}: {energy}%")

