# ============================================================
#  Project Title : Simple Calculator
#  Author        : Python Intern
#  Level         : Beginner (Level 1 Internship Task)
#  Description   : A menu-driven calculator that performs
#                  Addition, Subtraction, Multiplication,
#                  and Division on two user-provided numbers.
# ============================================================


# ---------- Operation Functions ----------

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """
    Return the quotient of a divided by b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed!")
    return a / b


# ---------- Display Menu ----------

def display_menu():
    """Print the operation menu to the console."""
    print("\n========================================")
    print("        SIMPLE CALCULATOR               ")
    print("========================================")
    print("  Select an operation:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Exit")
    print("========================================")


# ---------- Get Number Input ----------

def get_number(prompt):
    """
    Prompt the user for a number.
    Keeps asking until a valid float is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input! Please enter a numeric value.")


# ---------- Main Program ----------

def main():
    """Main function to run the calculator."""
    print("\nWelcome to the Simple Calculator!")

    while True:
        display_menu()

        choice = input("  Enter your choice (1-5): ").strip()

        # Exit option
        if choice == "5":
            print("\nThank you for using the Simple Calculator. Goodbye!\n")
            break

        # Validate menu choice
        if choice not in ("1", "2", "3", "4"):
            print("\n  Invalid choice! Please select a number between 1 and 5.")
            continue

        # Get two numbers from the user
        num1 = get_number("  Enter the first number  : ")
        num2 = get_number("  Enter the second number : ")

        # Perform the selected operation
        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        elif choice == "4":
            try:
                result = divide(num1, num2)
                operator = "/"
            except ZeroDivisionError as e:
                print(f"\n  {e}")
                continue

        # Display the result
        print(f"\n  Result : {num1} {operator} {num2} = {result}")


# ---------- Entry Point ----------

if __name__ == "__main__":
    main()
