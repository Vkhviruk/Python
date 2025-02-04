class Victoria:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        start_college_year = 2023
        age_start_college = start_college_year - self.birth_year
        course = age - age_start_college if age >= age_start_college else 0
        return course if 1 <= course <= 4 else "Помилка у визначенні курсу"

    def create_name_list(self):
        return [self.first_name, self.last_name]

person = Victoria("Victoria", "Khviruk", 2008)
print("Курс:", person.calculate_course())
print("Ім'я та прізвище:", person.create_name_list())

person_default = Victoria()
print("Курс (default):", person_default.calculate_course())
print("Ім'я та прізвище (default):", person_default.create_name_list())