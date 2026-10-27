class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Original Bill Amount: {self.bill_amount}")
        print(f"Final Bill Amount: {self.bill_amount}")
    @property
    def name(self):
        return self._name

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, new_bill_amount):
        if new_bill_amount < 0:
            print("Bill amount cannot be negative.")
        else:
            self._bill_amount = new_bill_amount

class Senior(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Original Bill Amount: {self.bill_amount}")
        print(f"Final Bill Amount: {self.bill_amount * 0.8}")

    @property
    def bill_amount(self):
            return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, new_bill_amount):
        if new_bill_amount < 0:
            print("Bill amount cannot be negative.")
        else:
            self._bill_amount = new_bill_amount
            self.new_bill_amount = new_bill_amount * 0.8

class PhilHealth(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    @property
    def bill_amount(self):
        return self._bill_amount

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Original Bill Amount: {self.bill_amount}")
        print(f"Final Bill Amount: {self.bill_amount * 0.85}")

    @bill_amount.setter
    def bill_amount(self, new_bill_amount):
        if new_bill_amount < 0:
            print("Bill amount cannot be negative.")
        else:
            self._bill_amount = new_bill_amount
            self.new_bill_amount = new_bill_amount * 0.85

reg_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = Senior("Maria Santos", 15000)
philhealth_patient = PhilHealth("Pedro Reyes", 15000)

print("Hospital Billing System:")
print("---")
reg_patient.display_info()
print("---")
senior_patient.display_info()
print("---")
philhealth_patient.display_info()
