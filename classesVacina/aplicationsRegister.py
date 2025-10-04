class Applications:

    def __init__(self, code_pacient, code_vaccine, applied_doses):
        self.pacient = code_pacient
        self.vaccine = code_vaccine
        self.dose = applied_doses
    
    def __str__(self):
        return f"Paciente: {self.pacient}, Vacina: {self.vaccine}, Dose: {self.dose}"