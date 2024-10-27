from Student import Student
from CollegeStudent import CollegeStudent
from HighschoolStudent import HighschoolStudent
import random

iran = Student("IRAN FERREIRA", "111", "18", 3)
ronaldo = Student("RONALDO FENOMENO", "222", "52", 3)
cassio = CollegeStudent("GOLEIRO CASSIO", "333", "45", 3)
ronaldinho = HighschoolStudent("RONALDINHO GAUCHO", "444", "32", 3)

print(iran<ronaldo)
print(iran>ronaldo)
print(iran==ronaldo)
print()

lista_student = [iran, ronaldo, cassio, ronaldinho]
random.shuffle(lista_student)
lista_student.sort()

for student in lista_student:
    print(student)
    print(Student.listType(student))
    print()