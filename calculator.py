print("===== MATHEMATICAL CALCULATOR =====")

while True:
    print("Choose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Clear")
    print("8. OFF")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Calculator OFF")
        break

    elif choice == "7":
        print("\n" * 20)
        print("Calculator Cleared")

    elif choice in ["1", "2", "3", "4", "5", "6"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", num1 + num2)

        elif choice == "2":
            print("Answer =", num1 - num2)

        elif choice == "3":
            print("Answer =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Division by zero is not allowed.")

        elif choice == "5":
            print("Answer =", num1 % num2)

        elif choice == "6":
            print("Answer =", num1 ** num2)

    else:
        print("Invalid Choice")