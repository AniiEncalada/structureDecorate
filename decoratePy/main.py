from domain.Student import Student
from domain.SocialEconomicLevel import SocialEconomicLevelEnum
from decorators.PersonDecorator import PersonBonus
from domain.Teacher import Teacher
from decorators.PersonDecorator import PersonExtraHours
from domain.AdministrativePersonal import AdministrativePersonal
from decorators.PersonDecorator import PersonExtraHoursAndBonus

# This is the main file. It is used to run the application. It creates instances of the Student, Teacher, and AdministrativePersonal classes and calls the task method on them. It also creates instances of the PersonBonus, PersonExtraHours, and PersonExtraHoursAndBonus classes and calls the task method on them. It demonstrates the use of the decorator pattern to add extra functionality to the Person class.
print("Default behavior")

# These are the instances of the Student, Teacher, and AdministrativePersonal classes. They are used to create objects with the attributes of a student, teacher, and administrative personal. The Student class is used to create a student object with the attributes of a student. The Teacher class is used to create a teacher object with the attributes of a teacher. The AdministrativePersonal class is used to create an administrative personal object with the attributes of an administrative personal.
student = Student(name="Matilde", socialEconomicLevel=SocialEconomicLevelEnum.LOW, last_name="Gonzalez", birth_date="1990-01-01", dni="12345678")
print(student.task())

teacher = Teacher(academicDegree="PhD", name="Juan", last_name="Perez", birth_date="1980-01-01", dni="87654321")
print(teacher.task())

administrative_personal = AdministrativePersonal(charge="Manager", name="Carlos", last_name="Gomez", birth_date="1970-01-01", dni="45678912")
print(administrative_personal.task())

print("\n")
print("Decorated behavior")
# These are the instances of the PersonBonus, PersonExtraHours, and PersonExtraHoursAndBonus classes. They are used to create objects with the attributes of a person with extra hours, bonus, and extra hours and bonus. The PersonBonus class is used to create a person object with the attributes of a person with bonus. The PersonExtraHours class is used to create a person object with the attributes of a person with extra hours. The PersonExtraHoursAndBonus class is used to create a person object with the attributes of a person with extra hours and bonus.
student = PersonBonus(student)
print(student.task())

teacher = PersonExtraHours(teacher)
print(teacher.task())

administrative_personal = PersonExtraHoursAndBonus(administrative_personal)
print(administrative_personal.task())

print("\n")
print("Decorated behavior with multiple decorators")
student = PersonExtraHours(student)
print(student.task())

teacher = PersonBonus(teacher)
print(teacher.task())

print("\n")
personal = AdministrativePersonal(charge="Manager", name="Carlos", last_name="Gomez", birth_date="1970-01-01", dni="45678912")
personal = PersonExtraHours(personal)
print(personal.task())