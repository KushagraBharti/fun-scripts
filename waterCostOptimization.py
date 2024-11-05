def calculate_yearly_cost():
    # Collect user inputs
    print("Enter details for the Brita-like filter dispenser:")
    dispenser_cost = float(input("Cost of dispenser (one-time fee): "))
    filter_cost = float(input("Cost per filter: "))
    filter_capacity = float(input("Filter capacity in liters: "))

    print("\nEnter details for buying water bottles:")
    pack_cost = float(input("Cost per 40-pack of water: "))
    bottle_volume = float(input("Volume per bottle in liters (typical 0.5L): "))

    daily_consumption = float(input("\nHow many liters of water do you drink per day? "))

    # Calculations for filter dispenser
    yearly_consumption = daily_consumption * 365
    filters_needed = yearly_consumption / filter_capacity
    yearly_filter_cost = filters_needed * filter_cost
    total_dispenser_cost = dispenser_cost + yearly_filter_cost

    # Calculations for bottled water
    bottles_needed_daily = daily_consumption / bottle_volume
    packs_needed_daily = bottles_needed_daily / 40
    yearly_packs_needed = packs_needed_daily * 365
    total_bottled_water_cost = yearly_packs_needed * pack_cost

    # Displaying the results
    print("\nYearly Costs Comparison:")
    print(f"Filter Dispenser: ${total_dispenser_cost:.2f} per year")
    print(f"Bottled Water: ${total_bottled_water_cost:.2f} per year")

    if total_dispenser_cost < total_bottled_water_cost:
        print("The filter dispenser is cheaper.")
    else:
        print("Buying bottled water is cheaper.")

# Run the comparison
calculate_yearly_cost()
