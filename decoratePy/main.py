from domain.Student import Student
from domain.SocialEconomicLevel import SocialEconomicLevelEnum
from decorators.PersonDecorator import PersonBonus
from domain.Teacher import Teacher
from decorators.PersonDecorator import PersonExtraHours
from domain.AdministrativePersonal import AdministrativePersonal
from decorators.PersonDecorator import PersonExtraHoursAndBonus

print("Default behavior")
student = Student(name="Matilde", socialEconomicLevel=SocialEconomicLevelEnum.LOW, last_name="Gonzalez", birth_date="1990-01-01", dni="12345678")
print(student.task())

teacher = Teacher(academicDegree="PhD", name="Juan", last_name="Perez", birth_date="1980-01-01", dni="87654321")
print(teacher.task())

administrative_personal = AdministrativePersonal(charge="Manager", name="Carlos", last_name="Gomez", birth_date="1970-01-01", dni="45678912")
print(administrative_personal.task())

print("\n")
print("Decorated behavior")
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