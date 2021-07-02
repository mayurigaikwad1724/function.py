def menu(day):
    if day == "monday":
        return "Butter Chicken"
    elif day == "tuesday":
        return "Mutton Chaap"
    elif day == "wednesday":
        return "matar panir"
    else:
        return "Chole Bhature"

    print ("Kya main print ho payungi? :-(")

mon_menu = menu("monday")
print (mon_menu)
tues_menu = menu("tuesday")
print (tues_menu)
wed_menu = menu("wednesday")
print (wed_menu)
fri_menu = menu("friday")
print (fri_menu) 

def Addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def divide(x, y):
    return x / y
def multiplication(x, y):
    return x * y
print("Select the oprator.")
print("press 1 for Addition")
print("press 2 for Subtraction")
print("press 3 for divide")
print("press 4 for multiplication")
while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        num1 =float(input("Enter the first number: "))
        num2 =float(input("Enter the second number: "))
        if choice == '1':
            print(num1, "+", num2, "=", Addition(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))
        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '4':
            print(num1, "*", num2, "=", multiplication(num1, num2))
        break
    else:
        print("Invalid")