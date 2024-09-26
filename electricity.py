def calculate_electricity_bill(units):
    # Define rates (in this example, we use a hypothetical rate per unit)
    rate_per_unit = 3 # Example rate per unit in INR

    if units <= 200:
        return 0  # Free for units up to 200
    else:
        # Calculate bill for units exceeding 200
        excess_units = units - 200
        bill_amount = excess_units * rate_per_unit
        return bill_amount

def main():
    try:
        # Input the number of units consumed
        units = float(input("Enter the number of electricity units consumed: "))
        
        if units < 0:
            print("Units consumed cannot be negative. Please enter a valid number.")
            return

        bill = calculate_electricity_bill(units)
        print(f"The electricity bill for {units} units is: INR {bill:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numerical value for units.")

if __name__ == "__main__":
    main()
