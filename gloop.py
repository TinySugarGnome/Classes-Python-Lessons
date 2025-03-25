""" import json

class Car:
    def __init__(self, make, model, year, image=None):
        self.make = make
        self.model = model
        self.year = year
        self.image = image
    
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image} """

""" class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

# Student Class
class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
    def abilities(self):
        return"you get to do this"

# Teacher Class
class Teacher(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    def abilities(self):
        return"teacher hii meow"

# Administrator Class
class Administrator(User):
    def __init__(self, name, email, password, role):
        super().__init__(name, email, password)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    def abilities(self):
        return"oh ur an administator"


users_data = {
    "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
    "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
    "johnson@example.com": Administrator("Ms. Johnson", "johnson@example.com", "adminpass", "Principal")
}











def login():
    email = input("Enter your email to log in: ")
    password = input("Enter your password: ")
    user = users_data.get(email)
    
    if user and user.password == password:
        print(user.display_info())
        print(user.abilities())
    else:
        print("Invalid email or password.")

# Call the login function
login()
 """

flashcards = {}

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

# Student Class
class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
    def abilities(self):
        global flashcards 
        while True:
            for key, value in flashcards.items():
                question = key
                answer = value
                hi = input(f'so the question is like {question}') 
                if hi == answer:
                    return 'correct'
                else:
                    return 'incorrect'
# Teacher Class
class Teacher(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

    def abilities(self):
        global flashcards  
        while True:
            makeone = input('Make a flashcard (format: key,value) or type "stop" to end: ')
            
            if makeone.lower() == 'stop':
                break
            key, value = makeone.split(',', 1)  # Limit to 1 split look AT IT
            flashcards[key.strip()] = value.strip()  
            print(f"Flashcard created: Key = '{key.strip()}', Value = '{value.strip()}'")

# Administrator Class
class Administrator(User):
    def __init__(self, name, email, password, role):
        super().__init__(name, email, password)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def abilities(self):
        return "oh ur an administrator"

users_data = {
    "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
    "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
    "johnson@example.com": Administrator("Ms. Johnson", "johnson@example.com", "adminpass", "Principal")
}

def login():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    user = users_data.get(email)
    
    if user and user.password == password and user.name == name:
        print(user.display_info())
        print(user.abilities())
    else:
        print("Invalid name, email, or password.")
login()

""" def login():
    email = input("Enter your email to log in: ")
    password = input("Enter your password: ")
    user = users_data.get(email)
    
    if user and user.password == password:
        print(user.display_info())
        print(user.abilities())
    else:
        print("Invalid email or password.")

# Call the login function
login() """
