

def calculate_total(marks):
    return sum(marks.values())

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def has_passed(marks):
    return all(mark >= 35 for mark in marks.values())
