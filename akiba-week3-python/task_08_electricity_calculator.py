def validate_units(units):
    return units >= 0


def calculate_tier_charges(units):
    first_tier = min(units, 50) * 0.50

    second_tier = min(max(units - 50, 0), 100) * 0.75

    third_tier = max(units - 150, 0) * 1.20

    return first_tier, second_tier, third_tier


def calculate_bill(units, service_fee=0):
    if not validate_units(units) or service_fee < 0:
        return None

    first, second, third = calculate_tier_charges(units)

    return first + second + third + service_fee


def billing_summary(units, service_fee=0):
    if not validate_units(units) or service_fee < 0:
        return "Invalid units or service fee."

    first, second, third = calculate_tier_charges(units)
    total = calculate_bill(units, service_fee)

    return {
        "Units consumed": units,
        "First 50 units": first,
        "Next 100 units": second,
        "Above 150 units": third,
        "Service fee": service_fee,
        "Total bill": total
    }


units = float(input("Enter electricity units consumed: "))
service_fee = float(input("Enter service fee (0 if none): "))

summary = billing_summary(units, service_fee)

if isinstance(summary, dict):
    print("\n--- Electricity Billing Summary ---")

    for item, amount in summary.items():
        print(f"{item}: {amount:.2f} Birr")
else:
    print(summary)
