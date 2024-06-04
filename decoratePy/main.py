from domain.Student import Student
from domain.SocialEconomicLevel import SocialEconomicLevelEnum
from decorators.PersonDecorator import PersonBonus
from domain.Teacher import Teacher
from decorators.PersonDecorator import PersonExtraHours
from domain.AdministrativePersonal import AdministrativePersonal
from decorators.PersonDecorator import PersonExtraHoursAndBonus

student = Student(name="Matilde", socialEconomicLevel=SocialEconomicLevelEnum.LOW, last_name="Gonzalez", birth_date="1990-01-01", dni="12345678")
print(student.task())

student_bonus = PersonBonus(student)
print(student_bonus.task())

teacher = Teacher(academicDegree="PhD", name="Juan", last_name="Perez", birth_date="1980-01-01", dni="87654321")
print(teacher.task())

teacher_extra_hours = PersonExtraHours(teacher)
print(teacher_extra_hours.task())

administrative_personal = AdministrativePersonal(charge="Manager", name="Carlos", last_name="Gomez", birth_date="1970-01-01", dni="45678912")
print(administrative_personal.task())

administrative_personal_extra_hours_bonus = PersonExtraHoursAndBonus(administrative_personal)
print(administrative_personal_extra_hours_bonus.task())