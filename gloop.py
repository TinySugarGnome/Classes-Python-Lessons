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
login() """

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



""" import json

flashcards = {}

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
    def abilities(self):
        while True:
            for question, answer in flashcards.items():
                user_answer = input(f'Question: {question} ')
                if user_answer == answer:
                    print('Correct!')
                else:
                    print('Incorrect!')

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "student_id": self.student_id,
        }

class Teacher(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

    def abilities(self):
        while True:
            makeone = input('Make a flashcard or type "stop" to end: ')
            if makeone.lower() == 'stop':
                break
            key, value = makeone.split(',', 1)
            flashcards[key.strip()] = value.strip()  
            print(f"Flashcard created: Key = '{key.strip()}', Value = '{value.strip()}'")

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subject": self.subject,
        }

# Create users
users_data = {
    "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
    "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
}

# Convert users data to a serializable format
serializable_data = {
    key: value.to_dict() for key, value in users_data.items()
}

# Save to JSON file
with open("gloopy.json", "w") as file:
    json.dump(serializable_data, file, indent=4)

def login():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    user = users_data.get(email)
    
    if user and user.password == password and user.name == name:
        print(user.display_info())
        user.abilities()
    else:
        print("Invalid name, email, or password.")

login()
 """


""" 
import json

flashcards = {}

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
    
    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    
    def abilities(self):
        while True:
            for question, answer in flashcards.items():
                user_answer = input(f'Question: {question} ')
                if user_answer == answer:
                    print('Correct!')
                else:
                    print('Incorrect!')

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "student_id": self.student_id,
        }

class Teacher(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

    def add_flashcard(self, key, value):
        flashcards[key.strip()] = value.strip()
        self.save_flashcards()

    def save_flashcards(self):
        with open("skibidi.json", "w") as file:
            json.dump(flashcards, file, indent=4)

    def abilities(self):
        while True:
            makeone = input('Make a flashcard or type "stop" to end: ')
            if makeone == 'stop':
                break
            key, value = makeone.split(',', 1)
            self.add_flashcard(key, value)
            print(f"Flashcard created: Key = '{key}', Value = '{value}'")

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subject": self.subject,
        }

# Create users
users_data = {
    "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
    "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
}

# Convert users data to a serializable format
serializable_data = {
    key: value.to_dict() for key, value in users_data.items()
}

# Save users data to JSON file
with open("gloopy.json", "w") as file:
    json.dump(serializable_data, file, indent=4)

def login():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    user = users_data.get(email)
    
    if user and user.password == password and user.name == name:
        print(user.display_info())
        user.abilities()
    else:
        print("Invalid name, email, or password.")

login() """



""" import json

def load_flashcards(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Flashcard file not found.")
        return {}

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.flashcards = {} 

    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

    def abilities(self):
        self.flashcards = load_flashcards("skibidi.json")  # Loads
        correct_answers = 0
        total_questions = 0
        streak = 0
        bonus_points = 0
        stopinput = input('')
        while True:
            for question, answer in self.flashcards.items():
                user_answer = input(f'Question: {question} ')
                total_questions += 1
                if user_answer.strip() == answer.strip():
                    print('Correct!')
                    correct_answers += 1
                    streak += 1
                    if streak % 3 == 0:
                        bonus_points += 1 
                        print(f'Bonus point awarded Total bonus points: {bonus_points}')
                else:
                    print(f'Incorrect The correct answer is: {answer}')
                    streak = 0  
                if user_answer == 'stop' or stopinput.strip().lower() == 'stop':
                    break
                    
            print(f'You got {correct_answers} out of {total_questions} correct. Bonus points: {bonus_points}')
            break


class Teacher(User):
    flashcards = {}  

    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
    
    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

    def save_flashcards(self):
        with open("skibidi.json", "w") as file:
            json.dump(Teacher.flashcards, file, indent=4)
            
    def add_flashcard(self, key, value):
        Teacher.flashcards[key] = value
        self.save_flashcards()


    def abilities(self):
        while True:
            makeone = input('Make a flashcard or type "stop" to end: ')
            if makeone.lower() == 'stop':
                break
            try:
                key, value = makeone.split(',', 1) #only allows 1 comma
                self.add_flashcard(key, value)
                print(f"Flashcard created: Key = '{key.strip()}', Value = '{value.strip()}'")
            except ValueError:
                print('you cant make that formatttt')

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subject": self.subject,
        }

users_data = {
    "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
    "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
}
with open("gloopy.json", "w") as file:
    json.dump({key: value.__dict__ for key, value in users_data.items()}, file, indent=4)


def login():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    user = users_data.get(email)
    
    if user and user.password == password and user.name == name:
        print(user.display_info())
        user.abilities()
    else:
        print("Invalid name, email, or password.")


login() """

""" import json

def load_flashcards(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Flashcard file not found.")
        return {}

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.flashcards = load_flashcards("skibidi.json")  #

    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

    def abilities(self):
        correct_answers = 0
        total_questions = 0
        streak = 0
        bonus_points = 0

        while True:
            for question, answer in self.flashcards.items():
                user_answer = input(f'Question: {question} (type "stop" to end): ')
                if user_answer.strip().lower() == "stop":
                    print(f'You got {correct_answers} out of {total_questions} correct. Bonus points: {bonus_points}')
                    return

                total_questions += 1
                if user_answer.strip() == answer.strip():
                    print('Correct!')
                    correct_answers += 1
                    streak += 1
                    if streak % 3 == 0:
                        bonus_points += 1
                        print(f'Bonus point awarded! Total bonus points: {bonus_points}')
                else:
                    print(f'Incorrect! The correct answer is: {answer}')
                    streak = 0

class Teacher(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
        self.flashcards = {}  

    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

    def abilities(self):
        while True:
            makeone = input('Make a flashcard (format: question,answer) or type "stop" to end: ')
            if makeone.lower() == 'stop':
                break
            try:
                key, value = makeone.split(',', 1)  # allows 1 comma cuz 1 vlaue
                self.flashcards[key.strip()] = value.strip()  
                self.save_flashcards() 
                print(f"Flashcard created: Key = '{key.strip()}', Value = '{value.strip()}'")
            except ValueError:
                print('Invalid format. Please use "question,answer".')

    def save_flashcards(self):
        with open("skibidi.json", "w") as file:
            json.dump(self.flashcards, file, indent=4)

def login():
    users_data = {
        "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
        "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
    }

    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    user = users_data.get(email)
    
    if user and user.password == password and user.name == name:
        print(user.display_info())
        user.abilities()
    else:
        print("Invalid name, email, or password.")

login() """


import json

class Flashcards:
    def __init__(self, filename):
        self.filename = filename
        self.flashcards = self.load_flashcards()

    def load_flashcards(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Flashcard file not found.")
            return {}

    def save_flashcards(self):
        with open(self.filename, "w") as file:
            json.dump(self.flashcards, file, indent=4)

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.flashcards_manager = Flashcards("skibidi.json")

    def display_info(self):
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

    def abilities(self):
        correct_answers = 0
        total_questions = 0
        streak = 0
        bonus_points = 0

        while True:
            for question, answer in self.flashcards_manager.flashcards.items():
                user_answer = input(f'Question: {question} (type "stop" to end): ')
                if user_answer.strip().lower() == "stop":
                    print(f'You got {correct_answers} out of {total_questions} correct. Bonus points: {bonus_points}')
                    return

                total_questions += 1
                if user_answer.strip() == answer.strip():
                    print('Correct!')
                    correct_answers += 1
                    streak += 1
                    if streak % 3 == 0:
                        bonus_points += 1
                        print(f'Bonus point awarded! Total bonus points: {bonus_points}')
                else:
                    print(f'Incorrect! The correct answer is: {answer}')
                    streak = 0

class Teacher(User):
    def __init__(self, name, email, password, subject):
        super().__init__(name, email, password)
        self.subject = subject
        self.flashcards_manager = Flashcards("skibidi.json")

    def display_info(self):
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"

    def abilities(self):
        while True:
            makeone = input('Make a flashcard (format: question,answer) or type "stop" to end: ')
            if makeone.lower() == 'stop':
                break
            try:
                key, value = makeone.split(',', 1)
                self.flashcards_manager.flashcards[key.strip()] = value.strip()
                self.flashcards_manager.save_flashcards()
                print(f"Flashcard created: Key = '{key.strip()}', Value = '{value.strip()}'")
            except ValueError:
                print('Invalid format. Please use "question,answer".')

def login():
    users_data = {
        "alice@example.com": Student("Alice", "alice@example.com", "password123", "S12345"),
        "smith@example.com": Teacher("Mr. Smith", "smith@example.com", "teacherpass", "Mathematics"),
        "denis@example.com": Teacher("Mr. Denis", "denis@example.com", "imdenis", "CompSci"),
    }

    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    user = users_data.get(email)
    
    if user and user.password == password:
        print(user.display_info())
        user.abilities()
    else:
        print("Invalid email or password.")
login()