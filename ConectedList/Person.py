class Person:
    def __init__(self, name, education, speciality, year_of_born, stage):
        self.__name = name
        self.__education = education
        self.__speciality = speciality
        self.__year_of_born = year_of_born
        self.__stage = stage

    def get_year_of_born(self):
        return self.__year_of_born

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_speciality(self):
        return self.__speciality

    def get_stage(self):
        return self.__stage