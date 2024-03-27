students_list = []
students_dict = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    students_list.append(name) #adding to list using append func.
    students_dict[name] = {'age': age, 'grade': grade} # nastal dictionary 

    print(f"Student {name} added successfully!")
    print("Updated Student Information:")
    print(students_dict)

def search_student():
    name = input("Enter student name to search: ")
    if name in students_dict:
        print(f"Student found!\nName: {name}\nAge: {students_dict[name]['age']}\nGrade: {students_dict[name]['grade']}") # searching in list and calling keys
    else:
        print(f"Student {name} not found in the system.")

def remove_student():
    name = input("Enter student name to remove: ") #user input
    if name in students_dict:
        students_list.remove(name) #straight forward using name to remove
        del students_dict[name]
        print(f"Student {name} removed successfully!")
        print("Updated Student Information:")
        print(students_dict)
    else:
        print(f"Student {name} not found in the system.")

# Test the system
add_student()
search_student()
remove_student()
