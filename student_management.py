import json

class student :
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)    
    def __str__(self):
        return f"Student:{self.name},Average:{self.calculate_average()},"
    def to_dict(self):
        return{
            "type": "student",
            "name": self.name,
            "grades": self.grades
        }
    
class course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.students = []
    def add_student(self,student):  
        self.students.append(student)
    def get_top_student(self):
        if not self.students: 
            return None
        top_avg = 0
        top_student = None
        for student in self.students:
            if student.calculate_average() > top_avg:
                top_avg = student.calculate_average()
                top_student = student
        return top_student
    def calculate_course_avg(self):
        if not self.students:
            return 0
        total_avg = 0
        for student in self.students:
            total_avg += student.calculate_average()
        return total_avg / len(self.students)    
    def __str__(self):
        return f"Course: {self.course_name} | Total Students: {len(self.students)} | Course Average: {self.calculate_course_avg()}"
    def save_to_file(self,filename="students.json"):
        data = [student.to_dict()for student in self.students]
        with open (filename,'w') as f:
                json.dump(data, f, indent=4)
        print("data saved successfully!")
    def load_from_file(self,filename="students.json"):
        try:
            with open(filename,"r") as f:
                data = json.load(f)
                for item in data:
                    if item["type"] == "student":
                        s = student(item["name"],item["grades"])
                    elif item["type"] == "graduate":
                        s = graduatestudent(item["name"],item["grades"],item["thesis"])
            self.add_student(s)
            print("data loaded successfuly!")
        except FileNotFoundError:
            print("no saved data found, starting fresh.")
class graduatestudent(student):
    def __init__(self, name, grades, thesis):
        super().__init__(name, grades)
        self.thesis = thesis
    def __str__(self):
        return f"Graduae Studente: {self.name}, Average: {self.calculate_average()},Thesis: {self.thesis}"
    def to_dict(self):
        data= super().to_dict()
        data["type"]="graduate"
        data["thesis"] = self.thesis
        return data
c1 = course("python course")
c1.load_from_file()
while True:
    print("""click => 1 to add new student" 
    click => 2 to add graduate student
    click => 3 to show the student 
    click => 4 to exit and save
""")
    choice = input("enter choice: ")
    if choice == "1":
        name = input("enter student name:")
        grades_input = input("enter grades (e.g 80 90 85): ")
        grades = [float(g) for g in grades_input.split()]
        new_student = student(name,grades)
        c1.add_student(new_student)
        print("Student Added Successfully!")
    elif choice == "2":
        name = input("enter student name:")
        grades_input = input("enter grades (e.g 80 90 85): ")
        grades = [float(g) for g in grades_input.replace(',', ' ').split()]
        thesis = input("enter thesis topic:")
        new_grad = graduatestudent(name,grades,thesis)
        c1.add_student(new_grad)
        print("Gradute Student Added Sessfull!")
    elif choice == "3":
        top_student = c1.get_top_student()
        if top_student :
            print("top student details:")
            print(top_student)
        else:
            print("no student in the course yet.")
    elif choice == "4":
        c1.save_to_file()
        print("Goodbye!")
        break
        
           