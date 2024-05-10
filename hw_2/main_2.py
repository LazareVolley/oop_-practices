import datetime


#Задание №1
class Patient:
    def __init__(self, name: str, age: int, disease: str, first_name: str, second_name: str, patronymic: str, day: int,
                 month: int, year: int, time):
        self.name = name
        self.age = age
        self.disease = disease
        self.first_name = first_name
        self.last_name = second_name
        self.patronymic = patronymic
        self.day = day
        self.month = month
        self.year = year
        self.time = time

    @staticmethod
    def meeting():
        """
        Ввод пользователем данных полей для заведения заявки клитента на приём
        :return: None
        """
        last_name = input()
        if not isinstance(last_name):
            print("В фамилии не может быть числовых значений!")

        first_name = input()
        if not isinstance(last_name):
            print("В имени не может быть числовых значений!")

        patronymic = input()
        if not isinstance(last_name):
            print("В отчестве не может быть числовых значений!")

        date = input('Введите дату формата (00.00.0000): ')
        if not date.isdigit():
            print("Введите дату формата (00.00.0000)")

        print(f" {datetime.date.today()} Запись клиента ({last_name}{first_name}{patronymic}) на {date}")


Patient.meeting()
