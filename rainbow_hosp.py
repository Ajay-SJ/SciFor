class Patient:
    def __init__(self, id, name, disease, doctor):
        self.id = id
        self.name = name
        self.disease = disease
        self.doctor = doctor

class Hospital:
    def __init__(self):
        self.patients = []

    def admit_patient(self, id, name, disease, doctor):
        new_patient = Patient(id, name, disease, doctor)
        self.patients.append(new_patient)

    def get_patient(self, search_term):
        for patient in self.patients:
            if patient.id == search_term or patient.name == search_term or patient.disease == search_term or patient.doctor == search_term:
                return patient
        return None

    def show_all_patients(self):
        for patient in self.patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Disease: {patient.disease}, Doctor: {patient.doctor}")

    def discharge_patient(self, search_term):
        self.patients = [patient for patient in self.patients if not (patient.id == search_term or patient.name == search_term or patient.disease == search_term or patient.doctor == search_term)]

hospital = Hospital()

while True:
    print("1. Admit patient")
    print("2. Get patient details")
    print("3. Show all patients")
    print("4. Discharge patient")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        doctor = input("Enter doctor in charge: ")
        hospital.admit_patient(id, name, disease, doctor)
    elif choice == 2:
        search_term = input("Enter patient ID or name or disease or doctor: ")
        patient = hospital.get_patient(search_term)
        if patient:
            print(f"ID: {patient.id}, Name: {patient.name}, Disease: {patient.disease}, Doctor: {patient.doctor}")
        else:
            print("No patient found.")
    elif choice == 3:
        hospital.show_all_patients()
    elif choice == 4:
        search_term = input("Enter patient ID or name or disease or doctor: ")
        hospital.discharge_patient(search_term)
    elif choice == 5:
        break
