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
        self.curator = "None"

    def add_curator(self, curator):
        self.curator = curator

    def show_info(self):
        super().show_info()
        print(f"Study in {self.academy} with this grades {' '.join(str(i) for i in self.__grades)}\nCurator is {self.curator}")


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
        self.students = []

    def add_student(self, *args):
        self.students.extend(args)

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, income):
        if income > 0:
            self.__income = income

    def show_info(self):
        super().show_info()
        students_name = ",".join(str(student_name) for student_name in self.students)
        print(f"Teaches in {self.academy} with income of {self.__income}\nStudents- {students_name}")


class Academy:
    def __init__(self, academ_name, corpuses, students):
        self.corpuses = corpuses
        self.students = students
        self.__academ_name = academ_name
        self.teachers = []

    def add_teacher(self, *args):
        self.teachers.extend(args)

    def show_info(self):
        teachers_names = ",".join(str(teacher_name) for teacher_name in self.teachers)
        print(f"There are {self.corpuses} corpuses in {self.__academ_name} with {self.students} students"
              f"\nTeachers in {self.academ_name}- {teachers_names}")

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
        self.faculty_teachers = []

    def add_fac_teacher(self, *args):
        self.faculty_teachers.extend(args)

    @property
    def dean_name(self):
        return self.__dean_name

    @dean_name.setter
    def dean_name(self, dean_name):
        if len(dean_name) > 2:
            self.__dean_name = dean_name

    def show_info(self):
        fac_teach_names = ",".join(str(teacher_name) for teacher_name in self.faculty_teachers)
        print(f"Faculty of {self.name}.\nStudents in faculty - {self.students}\nDepartments- {self.departments}."
              f"\nTeachers on faculty- {fac_teach_names}\nDean is {self.__dean_name}")


some_student1 = Student("Petya", 20, "DNU", [1, 1, 1, 1])
some_student2 = Student("Vasya", 23,"DNU", [3, 4, 5, 2, 4])
ilya_grades = [3, 4, 4, 5, 2]
ignat_grades = [5, 5, 5, 5]
teacher2 = Teacher("Vlad", 33, "DNU", 30000)
teacher = Teacher("Yulia", 25, "DNU", 25000)
teacher.add_student(some_student1.name, some_student2.name)
teacher.show_info()
print()
ightan = BudgetStudent("Ighnat", 19, "DNU", ignat_grades, 2000)
ilya = Student("Ilya", 20, "DNU", ilya_grades)
ilya.add_curator(teacher2.name)
ilya.show_info()
print()
ightan.add_curator(teacher.name)
ightan.show_info()
print()
teacher2.add_student(ilya.name, ightan.name)
teacher2.show_info()
print()
dnu = Academy("DNU", 15, 3000)
dnu.add_teacher(teacher.name, teacher2.name)
dnu.show_info()
print()
fuifm_dep = ["japan", "chinese", "turkish"]
fuifm = Faculty("FUIFM", 300, fuifm_dep, "Some Name")
fuifm.add_fac_teacher(teacher.name)
fuifm.show_info()
