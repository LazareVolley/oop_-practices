import datetime


#Задание №1
class Patient:
    def __init__(self, age: int, disease: str, first_name: str, second_name: str, patronymic: str, day: int,
                 month: int, year: int, time: int):
        self.age = age
        self.disease = disease
        self.first_name = first_name
        self.last_name = second_name
        self.patronymic = patronymic
        self.day = day
        self.month = month
        self.year = year
        self.time = time

    def meeting(self):
        """
        Ввод пользователем данных полей для заведения заявки клитента на приём
        :return: None
        """
        self.last_name = input()
        if not isinstance(self.last_name):
            print("В фамилии не может быть числовых значений!")

        self.first_name = input()
        if not isinstance(self.last_name):
            print("В имени не может быть числовых значений!")

        self.patronymic = input()
        if not isinstance(self.last_name):
            print("В отчестве не может быть числовых значений!")

        self.date = input('Введите дату формата (00.00.0000): ')
        if not self.date.isdigit():
            print("Введите дату формата (00.00.0000)")

        self.time = input('Введите время формата (00:00): ')
        if not self.time.isdigit():
            print("Введите дату формата (00:00)")

    def __str__(self):
        print(f" {datetime.date.today()} Запись клиента ({self.last_name}{self.first_name}{self.patronymic}) на {self.date}  в {self.time}")

patients = Patient(19, "Цефалгия", "Михаил", "Зубенко", "Петрович", 1, 1, 2024, 1345)


#Задание №2

class TouristSpot:
    def __init__(self, place_name: str, country: str, showplace_type: str):
        self.place_name = place_name
        self.country = country
        self.showplace_type = showplace_type

    def travel(self, visitor):
        print(f"Путешественник посещает место: {self.showplace_type} в {self.country}. Тип: {self.showplace_type}")

    def __str__(self):
        print(f"Путешественник посещает место: {self.showplace_type} в {self.country}.\nТип: {self.showplace_type}")

tourists = TouristSpot("Мамаев Курган", "Россия", "Историческая")