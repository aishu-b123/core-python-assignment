class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_avg(self):
        return sum(self.marks) / len(self.marks)

def top_performer(students):
    top_stu = None
    highest_avg = 0

    for name, marks in students.items():
        stu = Student(name, marks)
        avg = stu.calculate_avg()
        if avg > highest_avg:
            highest_avg = avg
            top_stu = name

    return top_stu, highest_avg

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}
top, highest_avg=top_performer(students)

print(f"Top Performer: {top} , average: {highest_avg:.2f}")
