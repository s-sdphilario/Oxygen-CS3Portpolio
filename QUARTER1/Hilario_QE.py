class Lab:
    def __init__ (self, room_number):
        self.room_number = room_number
class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj
        tech.assigned_lab.append(lab_obj)

lab = Lab("302")
tech = Technician("Mr. Cruz")

print(tech.assigned_lab.room_number)
tech.assign_lab(lab)