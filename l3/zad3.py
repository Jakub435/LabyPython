import time


class Patient:

    def __init__(self, fullName):
        self.fullName = fullName


class Doctor:
    queue = []

    def __init__(self, fullName, specialization):
        self.fullName=fullName
        self.specialization=specialization

    def addPatient(self, patient, priority):
        self.queue.append((priority, time.time(), patient))

    def getPatient(self):
        self.queue = sorted(self.queue, key=lambda x: (-x[0], x[1]))
        patient = self.queue[0][2]
        self.queue.remove(self.queue[0])
        return patient


class Clinic:
    doctors = []

    def addNewDoctor(self, doctor):
        self.doctors.append(doctor)

    def getDoctor(self, doctorFullName):
        for doctor in self.doctors:
            if(doctor.fullName == doctorFullName):
                return doctor

    def addPatientToDoctor(self, doctorFullName, patient, priority):
        self.getDoctor(doctorFullName).addPatient(patient, priority)

    def getNextPatient(self, doctorFullName):
        return self.getDoctor(doctorFullName).getPatient()

def main():
    clinic = Clinic()
    clinic.addNewDoctor(Doctor("Jan Kowalski", "Weterynarz"))
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak61"), 6)
    time.sleep(0.5)
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak0"), 0)
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak3"), 3)
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak2"), 2)
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak1"), 1)
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak5"), 5)
    clinic.addPatientToDoctor("Jan Kowalski", Patient("Marek Nowak62"), 6)

    for i in range(0, 7):
        print(clinic.getNextPatient("Jan Kowalski").fullName)


if __name__ == '__main__':
    main()
