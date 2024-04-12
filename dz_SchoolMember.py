import random
class SchoolMember:
    def __init__(self , name , surname):
        self.name = name
        self.surname = surname

class Teacher(SchoolMember):
    def __init__(self , name , surname, salary):
        super().__init__(name , surname)
        self.salary = salary

    def tell(self):
        return (f"Ім'я вчителя - {self.name}, прізвище - {self.surname}, зарплата - {self.salary}грн")

class Student(SchoolMember):
    def __init__(self, name , surname, rating):
        super().__init__( name , surname)
        self.rating  = rating

    def rozrahunok_serednyogo_baly(self):
        a=0
        for i in self.rating:
            a +=i
        b = a/len(self.rating)
        return b

    def tell(self):
        a = 0
        for i in self.rating:
            a += i
        b = a / len(self.rating)
        b_str = "{:.2f}".format(b)
        return (f"Ім'я учня - {self.name}, прізвище учня - {self.surname}, середній бал - {b_str}")

list_teachers = ['teach1','teach2','teach3','teach4']
list_student = ['student1','student2','student3','student4','student5','student6','student7',
                'student8','student9','student10']
list_names = ['Тарас','Іван','Ірина','Орест','Марія','Петро','Андрій','Назар','Олександр','Наталя']
list_surnames = ['Нирцузид','Чобіт','Зозуля','Фім','Хома','Карета','Михав','Галлета','Ютуз','Пінеклай']
rating_student1 = [1,2,3,4,5,6,7,8,9,10,11,12]

print('Список вчителів:\n')
for i in range(len(list_teachers)):
    rating_student9 = random.randint(1,9)
    salary = random.randrange(10000, 25000)
    list_teachers[i] = Teacher(list_names[rating_student9], list_surnames[i], salary)
    print(list_teachers[i].tell())

print('\n\nСписок учнів:\n')
for i in range(len(list_student)):
    rating_student = random.sample(rating_student1, 3)
    rating_student2 = random.randint(1,9)
    list_student[i] = Student(list_names[rating_student2], list_surnames[i],rating_student)
    print(list_student[i].tell())