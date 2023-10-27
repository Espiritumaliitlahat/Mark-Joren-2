import random

classroom_record = []

def generate_random_name():
    first_names = ['Juan', 'Maria', 'Jose', 'Carmen', 'Pedro', 'Ana', 'Antonio', 'Luis', 'Sofia', 'Miguel']
    last_names = ['Santos', 'Gonzalez', 'Rodriguez', 'Lopez', 'Martinez', 'Perez', 'Garcia', 'Fernandez', 'Reyes', 'Cruz']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def add_random_students(num_students):
    for _ in range(num_students):
        name = generate_random_name()
        classroom_record.append(name)

def remove_student(name):
    if name in classroom_record:
        classroom_record.remove(name)
    else:
        print(f"{name} is not in the classroom record.")

def display_classroom_record():
    print("Name Generator:")
    for i, name in enumerate(sorted(classroom_record)):
        print(f"{i+1}. {name}")


add_random_students(30)

display_classroom_record()
