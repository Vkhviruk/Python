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


class AdvancedVictoria(Victoria):
    def __init__(self, first_name=None, last_name=None, birth_year=None, city=None, college=None, major=None):
        super().__init__(first_name, last_name, birth_year)
        self.city = city
        self.college = college
        self.major = major
        self.__id_number = self._generate_id()

    def _generate_id(self):
        #Приватний метод для генерації унікального ідентифікатора студента
        import random
        return f"{self.last_name[:3].upper()}-{random.randint(1000, 9999)}" if self.last_name else None

    def get_id(self):
        #Публічний метод для отримання ID
        return self.__id_number

    def student_info(self):
        #Метод, що повертає інформацію про студента
        return {
            "Ім'я": self.first_name,
            "Прізвище": self.last_name,
            "Рік народження": self.birth_year,
            "Місто": self.city,
            "Коледж": self.college,
            "Спеціальність": self.major,
            "ID": self.__id_number
        }

student = AdvancedVictoria("Victoria", "Khviruk", 2008, "Lutsk", "ТФК ЛНТУ", "Computer Science")
print("Курс:", student.calculate_course())
print("Ім'я та прізвище:", student.create_name_list())
print("ID студента:", student.get_id())
print("Інформація про студента:", student.student_info())