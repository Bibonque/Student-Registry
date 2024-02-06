class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) >= 3 and new_name.istitle():
                self._name = new_name
            else:
                print("Name must contain only letters and be longer than two letters")
        else:
            print("Invalid input for name. Must be a string.")

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
        else:
            print("Invalid input for age. Must be an integer between 12 and 17.")

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade):
        valid_grades = ["9th", "10th", "11th", "12th"]
        if new_grade.endswith('th') and new_grade in valid_grades:
            self._grade = new_grade 
        else:
            print("Invalid input for grade. Must be formatted as '9th', '10th', '11th', or '12th'.")

    def __str__(self):
        return f"Student name: {self._name}, Age: {self._age}, Grade: {self._grade}"
        
    def advance(self, years_advanced=1):
        new_grade_number = int(self._grade[:-2]) + years_advanced
        new_grade = f"{new_grade_number}th"
        self._grade = new_grade  # Update the grade attribute
        print(f"{self.name} has advanced to the {new_grade} grade. Nerd")


    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

# Create a student
student1 = Student("Francisco", age=15, grade="12th")

# Print initial information
print(student1)

# Use setter methods
student1.name = "Frank"
student1.age = 16
student1.grade = "11th"

# Print updated information
print(student1)

# Test advance and study methods
student1.advance(1)
student1.study("Computer Science")
