#Reading two numbers
n1 = float(input("Enter first number :"))
n2 = float(input("Enter second number :"))
#Display menu
print("\n Choose operation:")
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")

choice = int(input("Enter your operation (1-4):" ))

# Performing Operations

if choice == 1:
    result = n1 + n2
    print(f"Result = {n1} + {n2} = {result}")
elif choice == 2:
    result = n1-n2
    print(f"Result = {n1} - {n2}= {result}")
elif choice == 3:
    result = n1 * n2
    print(f"Result = {n1} * {n2} = {result}")
elif choice == 4:
    if n2 !=0:
        result = n1/n2
        print(f"Result = {n1} / {n2} = {result}")
    else:

        print("Error : Division by Zero not possible")
else:
    print("Invalid Choice. Please enter 1-4")