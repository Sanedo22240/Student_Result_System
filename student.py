
from calculation import calculate_total, calculate_average, has_passed

class Student:
    def __init__(self, sid, name, marks):
        self.id = sid
        self.name = name
        self.marks = marks

    def total(self):
        return calculate_total(self.marks)

    def average(self):
        return calculate_average(self.marks)

    def has_passed(self):
        return has_passed(self.marks)

    def display(self):
        print(f"\nStudent ID: {self.id}")
        print(f"Name: {self.name}")
        for subject, mark in self.marks.items():
            print(f"{subject.title()}: {mark}")
        print(f"Total Marks: {self.total()}")
        print(f"Average Marks: {self.average():.2f}")
        print("Result:", "Pass" if self.has_passed() else "Fail")
