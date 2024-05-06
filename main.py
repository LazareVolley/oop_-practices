import random

#Задача №1
class Animal:
    def __init__(self, name: str, type: str, age: int, sound: str):
        """
        Конструктор
        :return: None
        """
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
        """
        Вывод полей констурктора (Ифнормация о животном)
        :return: None
        """
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
        """
        Конструктор
        :return: None
        """
        self.title = title
        self.author = author
        self.page_count = page_count

    def book_info(self):
        """
        Вывод полей конструктора (Информации о книге)
        :return: None
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

#Задача №3

class PassengerPlane:
    def __init__(self, manufacturer: str, plane_model: str, capacity: int, current_height: float, current_speed: int):
        """
        Конструктор
        :return: None
        """
        self.manufacturer = manufacturer
        self.plane_model = plane_model
        self.capacity = capacity
        self.current_height = current_height
        self.current_speed = current_speed

    def plane_information(self):
        """
        Вывод полей конструктора (Информации о самолёте)
        :return: None
        """
        print(f"Производитель: {self.manufacturer}")
        print(f"Модель самолёта: {self.plane_model} тип: пассажирский")
        print(f"Вместимость самолёта (Количество сидячих мест): {self.capacity} чел.")
        print(f"Текущая высота самолёта: {self.current_height}")
        print(f"Текущая скорость самолёта: {self.current_speed}")


    def airplane_takeoff(self):
        """
        Вывод полей конструктора (имитация взлёта самолё та)
        :return: None
        """
        self.current_height = f"{0.0} --> {random.uniform(2, 3)} --> {random.uniform(6, 8)}"
        self.current_speed = f"{0.0} --> {random.uniform(340, 360)}"
        print(f"Уважаемые пассажиры! Самолёт '{self.plane_model}' осуществляет взлёт! Текущая скорость: {self.current_speed}км/ч. Текущая высота: {self.current_height}м.")

    def airplane_flight(self):
        """
        Вывод полей конструктора (имитация полёта самолёта)
        :return:
        """
        self.current_height = random.uniform(860, 920)
        self.current_speed = f"{0.0} --> {random.uniform(840, 920)}"
        print(f"Уважаемые пассажиры! Текущая высота самолёта {self.plane_model} составляет {self.current_height}м., а его скорость равна {self.current_speed}км/ч.)")
        print("Пять минут - полёт нормальный!")

    def airplane_landing(self):
        """
        Вывод полей конструктора (имитация посадки самолёта)
        :return: None
        """
        self.current_height = f"{random.uniform(510, 400)} --> {random.uniform(380, 240)} --> {random.uniform(221, 157)}"
        self.current_speed = f"{random.uniform(97, 73)} --> {random.uniform(72, 64)} --> {random.uniform(60, 51)}"
        print(f"Уважаемые пассажиры! Просьба пристегнуть ремни безопасности, самолёт {self.plane_model} осуществляет посадку!\nТекущая высота: {self.current_height}м.\nТекущая скорость: {self.current_speed}км/ч.")

    def end_of_flight(self):
        """
        Вывод полей конструктора (имитация окончания полёта самолёта)
        :return: None
        """
        self.current_height = 0.0
        self.current_speed = 0.0
        print(f"Уважаемые пассажиры! Самолёт {self.plane_model} совершил успешную посадку! Благодарим, что выбрали нас!")


airplanes = PassengerPlane("Airbus", "A380−800", 853, 0.0, 0)
print(airplanes.plane_information())
print(airplanes.airplane_takeoff())
print(airplanes.airplane_flight())
print(airplanes.airplane_landing())
print(airplanes.end_of_flight())

#Задача №4

class MusicAlbum():
    def __init__(self = list, performer = str, album_title = str, music_genre = str):
        """
        Конструктор
        :return: None
        """
        self.performer = performer
        self.album_title = album_title
        self.music_genre = music_genre
        self.tracks = []

    def add_track_list(self, track: str):
        """
        Добавление строк в поле 'track_list'
        :return: None
        """
        self.tracks.append(track)
        print(self.tracks)

    def delete_track(self, track):
        """
        Поиск и даление строки из сприска 'tracks'
        :param track:
        :return:
        """
        if track in self.tracks:
            music = self.track.pop(track)
            print(f"Песня {music} удалена")
        else:
            print("Такой трек не найден в альбоме")

    def play_track(self, track):
        """
        Поиск строки в списке 'tracks'
        :param track:
        :return:
        """
        if track in self.tracks:
            print(f"Песня {track} воспроизведена...")
        else:
            print("Такой трек не найден в альбоме")

Albums = MusicAlbum("a-ha", "Hunting High and Low", "R&B / Pop")
print(Albums.add_track_list(track=input(">>")))
print(Albums.delete_track(track= input(">>")))
print(Albums.play_track(track= input(">>")))