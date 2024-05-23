#Задача №1.1 (Волшебник)
class Wizard:
    def __init__(self, name: str, faculty: str, force_level: int, spells_list: list, status: bool):
        self.__name = name
        self.__house = faculty
        self.__force_level = force_level
        self.__spells_list = spells_list
        self.__status = status

    def get_name(self):
        return self.__name

    def get_house(self):
        return self.__house

    def get_magic_level(self):
        return self.__force_level

    def get_spells(self):
        return self.__spells_list

    def get_status(self):
        return self.__status

    def set_house(self, faculty):
        self.__house = faculty

    def set_magic_level(self, force_level):

        if force_level < 0:
            return f"Значение {force_level} не может быть отрицательным"
        else:
            self.__force_level = force_level

    def set_status(self, status):
        self.__status = status

    def add_spell(self, spell):
        self.__spells_list += spell

    def remove_spell(self, spell):
        del spell

    def increase_magic_level(self, force_level: int):

        if force_level < 0:
            return f"Значение {force_level} не может быть отрицательным"
        else:
            self.__force_level += force_level

    def decrease_magic_level(self, force_level: int):

        if force_level < 0:
            return f"Значение {force_level} не может быть отрицательным"
        else:
            self.__force_level -= force_level

    def __str__(self):
        return wizard

wizard = Wizard("Ron Weasley", "gryffindor", 10, "Eat Slugs", True)

class Spels:
    pass

#Задача №1.2 (Заклинание)
class Spell:
    def __init__(self, title: str, level: int, spell_type: str, description: str):
        self.__title = title
        self.__level = level
        self.__spell_type = spell_type
        self.__description = description

    def get_title(self):
        return self.__title

    def get_level(self):
        return self.__level

    def get_spell_type(self):
        return self.__spell_type

    def get_description(self):
        return self.__description

    def set_title(self, title):
        self.__title = title

    def set_level(self, level):

        if level < 0 or level > 10:
            return f"Значение 'level' не может быть меньше 0 или больше 10!"
        else:
            self.__level = level

    def set_spell_type(self, spell_type: str):
        self.__spell_type = spell_type

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        return spell

spell = Spell("expecto patronum", 10, "explosive", "In order to use it, you must recall and feel your happiest memory (which is not easy with dementors), pull out your wand and say 'Expecto Patronum'")

#Задача №2. (Сотрудник)

class Employee:
    def __init__(self, name: str, position: str, department: str, salary: float, work_experience: int, completed_projects: list = None):
        self.__name = name
        self.__position = position
        self.__departament = department
        self.__salary = salary
        self.__work_experience = work_experience
        self.__completed_projects = completed_projects

    def get_name(self):
        return self.__name

    def get_position(self):
        return self.__position

    def get_departament(self):
        return self.__departament

    def get_salary(self):
        return self.__salary

    def get_work_experience(self):
        return self.__work_experience

    def get_completed_projects(self):
        return self.__completed_projects

    def set_position(self, position):
        self.__position = position

    def set_departament(self, position, departament):
        self.__departament = departament

    def pay_salary(self, salary):
        self.__salary = salary

    def add_projects(self, project):
        self.__completed_projects += project

    def delete_projects(self, project):
        del project

    def increase_salary(self, salary):
        self.__salary += salary

    def decrease_salary(self, salary):
        self.__salary -= salary

    def __str__(self):
        return employer

employer = Employee("Петя", "Недопрограммист", "IT-сервисы", 100.50, 10, ["Pet Project"])

#Задача №3. (Робот)

class Robot:
    def __init__(self, serial_number: str, model: str, current_task: str, battery_level: int, status: bool):
        self.__serial_number = serial_number
        self.__model = model
        self.__current_task = current_task
        self.__battery_level = battery_level
        self.__status = status

    def get_serial_number(self):
        return self.__serial_number

    def get_model(self):
        return self.__model

    def get_current_task(self):
        return self.__current_task

    def get_battery_level(self):
        return self.__battery_level

    def get_status(self):
        return self.__status

    def new_current_task(self, task):
        self.__current_task = task

    def del_current_task(self, task):
        del task

    def increase_battery_level(self, charge):

        if self.__battery_level + charge > 100:
            return f"Действие невозможно! Заряд превышает максимально возможное значение!"
        else:
            self.__battery_level += charge
    def decrease_battery_level(self, charge):

        if self.__battery_level - charge < 0:
            return f"Действие невозможно! Заряд менее минимально возможного значения!"
        else:
            self.__battery_level -= charge

    def turn_on_robot(self):

        if not self.__status:
            self.__status = True
    def pause_robot(self):

        if self.__status:
            self.__status = False

    def __str__(self):
        return robot

robot = Robot("FEG5*44YR$1T5&19E", "Wall-e", "relax", 100, False)

#Задача №4. (Атлет)

class Achievement:
    pass
class Athlete:
    def __init__(self, name: str, age: int, sport: str, status: bool, achievements: list = Achievement):
        self.__name = name
        self.__age = age
        self.__sport = sport
        self.__achievements = achievements
        self.__status = status

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sport(self):
        return self.__sport

    def get_achievements(self):
        return self.__achievements

    def get_status(self):
        return self.__status

    def set_age(self, age):
        self.__age = age

    def set_sport(self, sport):
        self.__sport = sport

    def set_status(self, status):
        self.__status = status

    def add_achievement(self, achievement: Achievement):
        self.__achievements.append(achievement)

    def delete_achievement(self, achievement: Achievement):
            self.__achievements.remove(achievement)

    def __str__(self):
        return athlete

athlete = Athlete("Grisha", 27, "Cricket", True, Achievement)

class Programm:
    @staticmethod
    def main():
        # Задача №1.1 (Волшебник)
        wizard = Wizard("Ron Weasley", "gryffindor", 10, "Eat Slugs", True)

        # Задача №1.2 (Заклинание)
        spell = Spell("expecto patronum", 10, "explosive","In order to use it, you must recall and feel your happiest memory (which is not easy with dementors), pull out your wand and say 'Expecto Patronum'")

        # Задача №2. (Сотрудник)
        employer = Employee("Петя", "Недопрограммист", "IT-сервисы", 100.50, 10, ["Pet Project"])

        # Задача №3. (Робот)
        robot = Robot("FEG5*44YR$1T5&19E", "Wall-e", "relax", 100, False)

        # Задача №4. (Атлет)
        athlete = Athlete("Grisha", 27, "Cricket", True, Achievement)