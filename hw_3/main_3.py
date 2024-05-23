#Задача №1.1
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

class Spell:
    pass