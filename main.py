#Задача №1
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        self.name = name
        self.type = type
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

#Задача №2

class Book:
    def __init__(self, title: str, author: str, page_count: int):
        self.title = title
        self.author = author
        self.page_count = page_count

    def book_info(self):
        """
        Вывод полей метода конструктора
        :return:
        """
        print(f"Название книги: '{self.title}'")
        print(f"Автор книги: {self.author}")
        print(f"Количество страниц в книге '{self.title}': {self.page_count}")

    def open_page(self):
        """
        Метод, который "позволяет пользователю выбрать страницу в кнгие"
        :return: None
        """

        while True:
            try:
                page = int(input(f"Количество страниц в книге: {self.page_count}\nВведите номер страницы, которую хотите открыть >> "))
                while page > self.page_count or page < 1:
                    print(f"ОШИБКА! Укажите страницы от 1 до {self.page_count}")
                    page = int(input(">> "))
                else:
                    print(f"Вы успешно открыли {page} страницу!")
                    break
            except ValueError:
                print("ОШИБКА! Вы можете указать только числовые значения! (1, 2, 3...)")


books = Book("Питон для начинающих", "Артур Пирожков", 80)
print(books.book_info())
print(books.open_page())