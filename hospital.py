class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease
def search_p(patients, disease):
    return [p.name for p in patients if p.disease.lower() == disease.lower()]
patients = [
    Patient("Alice", 30, "Flu"),
    Patient("Bob", 45, "Diabetes"),
    Patient("Charlie", 35, "Flu")
]
disease = "Flu"
result = search_p(patients,disease)

print(f"Patients with {disease}: {result}")
