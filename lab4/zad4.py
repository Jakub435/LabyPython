class Grade:

    def __init__(self, grade, weight):
        self.grade = grade
        self.weight = weight


class Student:
    grading = []

    def __init__(self, firstname, lastname):
        self.firstName = firstname
        self.lastName = lastname

    def addgrade(self, grade, weight):
        self.grading.append(Grade(grade, weight))

    def getaverage(self):
        gradesum = 0
        for el in self.grading:
            gradesum += el.grade

        return gradesum/len(self.grading)

    def getGrading(self):
        return self.grading


class Gradebook:
    students = []

    def loadstudents(self, students):
        self.students = students

    def addstudent(self, firstname, lastname):
        self.students.append(Student(firstname, lastname))

    def getstudent(self, firstname, lastname):
        for el in self.students:
            if(el.firstName == firstname and el.lastName == lastname):
                return el

    def addgrade(self, firstname, lastname, grade, weight):
        student = self.getstudent(firstname, lastname)
        if student:
            student.addgrade(grade, weight)
        print("No student")
        return

    def getstudentaveragegrade(self, firstname, lastname):
        student = self.getstudent(firstname, lastname)
        if student:
            return student.getaverage()
        print("No student")
        return None

    def getstudentgrades(self, firstname, lastname):
        student = self.getstudent(firstname, lastname)
        if student:
            return student.getGrading()
        print("No student")
        return None


class View:

    def __init__(self):
        gradebook = Gradebook()
        menu = "\n1-dodaj studenta\n2-dodaj ocene\n3-wyswietl oceny\n4-wyswietl średnią ocen\n5-zakończ\n"
        while True:
            opt = input(menu)

            firstName = input("Podaj imię: ")
            lastName = input("Podaj nazwisko: ")

            if opt == "1":
                gradebook.addstudent(firstName, lastName)
            elif opt == "2":
                grade = int(input("Podaj ocenę: "))
                weight = int(input("Podaj wagę: "))
                gradebook.addgrade(firstName, lastName, grade, weight)
            elif opt == "3":
                res = gradebook.getstudentgrades(firstName, lastName)
                if res:
                    for el in res:
                        print("ocena: " + str(el.grade) + "  waga: " + str(el.weight))
            elif opt == "4":
                res = gradebook.getstudentaveragegrade(firstName, lastName)
                if res:
                    print("średnia ocen: " + str(res))
            elif opt == "5":
                break


def main():
    View()


if __name__ == '__main__':
    main()
