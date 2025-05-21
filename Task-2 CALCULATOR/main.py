User_name = input("Please Enter your name: ")

def Calculate(Number1, Number2, Operation):
    if Operation == '+':
        print(f"{Number1} + {Number2} = {Number1 + Number2}")
    elif Operation == '-':
        print(f"{Number1} - {Number2} = {Number1 - Number2}")
    elif Operation == '*':
        print(f"{Number1} * {Number2} = {Number1 * Number2}")
    elif Operation == '/':
        if Number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{Number1} / {Number2} = {Number1 / Number2}")
    else:
        print("Invalid operation. Please choose from +, -, *, /.")

while True:
    User_response = input(f"Hello {User_name}, do you want to perform a calculation? (yes/no): ")

    if User_response.lower() == 'y' or User_response.lower() == 'yes':
        Number1 = int(input("Please Enter the first number: "))
        Number2 = int(input("Please Enter the second number: "))
        Operation = input("Choose your Mathematical operation (+, -, *, /): ")

        Calculate(Number1, Number2, Operation)

    elif User_response.lower() == 'n' or User_response.lower() == 'no':
        print(f"Thank you for using the calculator. Goodbye {User_name}!")
        break
    
    else:
        print("Invalid response. Please answer with 'yes' or 'no'.")
