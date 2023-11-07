def calculate_tax(income):
    if income < 10000:
        tax = 0
    elif income < 50000:
        tax = income * 0.05
    elif income < 100000:
        tax = income * 0.10
    else:
        tax = income * 0.15
    return tax

def main():
    while True:
        print("Tax Calculator Menu:")
        print("1. Calculate Tax")
        print("2. Quit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            income = float(input("Enter your income: "))
            tax = calculate_tax(income)
            print(f"Tax due on income ${income:.2f} is ${tax:.2f}")
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()