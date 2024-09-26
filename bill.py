# Default previous reading
previous_reading = 100  

# Input for current reading
current_reading = int(input("Enter the current reading (in units): "))

# Calculate used units
used_units = current_reading - previous_reading
print(f"\nUsed units: {used_units}")

# Calculate bill based on used units
if used_units <= 0:
    print("No units consumed. Bill: ₹0")
else:
    if used_units <= 200:
        bill = 0  # Gruha Jyothi Scheme
        print("Your bill is ₹0 due to the Gruha Jyothi Scheme (subsidy).")
    else:
        bill = (used_units - 200) * 3  # Charge for units above 200
        print(f"Charges for this month: ₹{bill}")
        print("Your bill is after applying subsidy for 200 units.")

