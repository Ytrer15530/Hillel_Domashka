class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 2 < len(name) <= 20:
            self.__name = name

    def show_info(self):
        print(f"I'm {self.__name} {self.age} years old")


class Student(Person):
    def __init__(self, name, age, academy, grades: list):
        super().__init__(name, age)
        self.academy = academy
        self.__grades = grades

    def show_info(self):
        super().show_info()
        print(f"Study in {self.academy} with this grades {' '.join(str(i) for i in self.__grades)}")


class BudgetStudent(Student):
    def __init__(self, name, age, academy, grades: list, scholarship=0):
        super().__init__(name, age, academy, grades)
        self.__scholarship = scholarship

    @property
    def scholarship(self):
        return self.__scholarship

    @scholarship.setter
    def scholarship(self, scholarship=0):
        try:
            if 0 < scholarship < 10000:
                self.__scholarship = scholarship
        except TypeError:
            print("Please enter int")

    def show_info(self):
        super().show_info()
        print(f"Scholarship is {self.__scholarship}")


class Teacher(Person):
    def __init__(self, name, age, academy, income):
        super().__init__(name, age)
        self.academy = academy
        self.__income = income

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, income):
        if income > 0:
            self.__income = income

    def show_info(self):
        super().show_info()
        print(f"Teaches in {self.academy} with income of {self.__income}")


class Academy:
    def __init__(self, academ_name, corpuses, students):
        self.corpuses = corpuses
        self.students = students
        self.__academ_name = academ_name

    def show_info(self):
        print(f"There are {self.corpuses} corpuses in {self.__academ_name} with {self.students} students")

    @property
    def academ_name(self):
        return self.__academ_name

    @academ_name.setter
    def academ_name(self, academ_name):
        if academ_name > 3:
            self.__academ_name = academ_name


class Faculty:
    def __init__(self, name, students, departments: list, dean_name):
        self.name = name
        self.students = students
        self.departments = departments
        self.__dean_name = dean_name

    @property
    def dean_name(self):
        return self.__dean_name

    @dean_name.setter
    def dean_name(self, dean_name):
        if len(dean_name) > 2:
            self.__dean_name = dean_name

    def show_info(self):
        print(f"Faculty of {self.name}.\nStudents in faculty - {self.students}\nDepartments- {self.departments}."
              f"\nDean is {self.__dean_name}")


ignat_grades = [5, 5, 5, 5]

ightan = BudgetStudent("Ighnat", 19, "DNU", ignat_grades, 2000)
ightan.show_info()
dnu = Academy("DNU", 15, 3000)
dnu.show_info()
fuifm_dep = ["japan", "chinese", "turkish"]
fuifm = Faculty("FUIFM", 300, fuifm_dep, "Some Name")
fuifm.show_info()
