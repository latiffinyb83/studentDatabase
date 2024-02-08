def display_student_info(index):
    print("Student's name:", names[index])
    category = input("Which category to display: Hometown or Favorite food? ").strip().lower()
    if category == "hometown":
        print("Hometown:", hometowns[index])
    elif category == "favorite food":
        print("Favorite food:", favorite_foods[index])
    else:
        print("Invalid category! Please enter either 'Hometown' or 'Favorite Food'.")
        display_student_info(index)

def print_student_list():
    print("\nList of students:")
    for i in range(len(names)):
        print(f"{i+1}. {names[i]}")

names = ["Alice", "Bob", "Charlie"]
hometowns = ["New York", "Los Angeles", "Chicago"]
favorite_foods = ["Pizza", "Sushi", "Burgers"]

print("Welcome to the Student Information System!")

while True:
    print_student_list()
    choice = input("Enter the number of the student you want to learn about or type 'quit' to exit: ").strip().lower()

    if choice == 'quit':
        print("Thank you for using the Student Information System. Goodbye!")
        break

    try:
        index = int(choice) - 1
        if index < 0 or index >= len(names):
            print("Invalid input! Please enter a number within the range.")
            continue
        display_student_info(index)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

    another = input("Would you like to learn about another student? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Thank you for using the Student Information System. Goodbye!")
        break
