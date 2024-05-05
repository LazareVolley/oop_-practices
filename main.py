#Задача №1
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name,
        self.type = type,
        self.age = age
        self.sound = sound

    def print_animal_sound(self):
        """
        Вывод поля "sound"
        :return: None
        """
        print(f"{self.name} издаёт звук: {self.sound}")

    def animal_information(self):
        print(f"Кличка: {self.name}")
        print(f"Вид животного:{self.type}")
        print(f"Возраст: {self.age}")
        print(f"Издаваемый звук: {self.sound}")

animals = Animal("Мурка", "Кошка", 6, "Мяу!") #Объект
print(animals.name, animals.type, animals.age, animals.sound)
print(animals.print_animal_sound())
print(animals.animal_information())