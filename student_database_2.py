# Dictionary
student_info = [
  { "name": "Tina", "hometown": "Portland", "favorite_food": "puppy chow" },
  { "name": "Klaus", "hometown": "Frankfurt", "favorite_food": "pizza" },
  { "name": "Julia", "hometown": "Houston", "favorite_food": "shrimp" }
]

# List of names/student info function
def list_names(student_info):
    index = 0
    for student in student_info:
        #student = dict(enumerate(student_info))
        index += 1
        print(index, student["name"])

    student_selection = int(input("Which student would you like to learn more about? "))

# Need to find a way to make the input accurate
    if 0 <= student_selection < len(student_info):
        student = student_info[student_selection]
        print(f"You selected {student['name']}")

        selection = input("What would you like to know? ")
        if "hometown" in selection:
            print(f"{student['name']}'s hometown is {student['hometown']}")
        elif "favorite food" in selection:
            print(f"{student['name']}'s favorite food is {student['favorite_food']}")

# Add new student function
def get_new_student():
    new_name = input("Enter name: ")
    new_homwtown = input("Enter hometown: ")
    new_food = input("Enter favorite food: ")
    new_student = {}
    new_student[0] = new_name
    new_student[1] = new_homwtown
    new_student[2] = new_food
    student_info.append({"name": new_name, "hometown": new_homwtown, "favorite_food": new_food})


# User input loop
while True:
    option_select = input("Select an option('add', 'view', 'quit'): ")
    if "quit" in option_select:
        print("Goodbye")
        break
    elif "view" in option_select:
        list_names(student_info)
    elif "add" in option_select:
        get_new_student()
