from datetime import datetime

# Meal plan data
meal_plans = {
    "Comet 19": {"price": 2478.41, "meals_per_week": 19},
    "Comet 14": {"price": 2189.42, "meals_per_week": 14},
    "Comet 10": {"price": 2071.91, "meals_per_week": 10}
}

# Function to calculate number of weeks and days between two dates
def calculate_weeks_and_days(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    total_days = (end - start).days
    total_weeks = total_days / 7
    return total_days, round(total_weeks, 2)

# Function to calculate the cost per meal based on meals eaten per week
def calculate_meal_costs_range(meal_plan, lower_weeks, upper_weeks):
    meals_per_week = meal_plans[meal_plan]["meals_per_week"]
    price = meal_plans[meal_plan]["price"]
    
    # Calculate cost per meal as a range (lower bound and upper bound for weeks)
    meal_costs = []
    for meals_eaten in range(meals_per_week, 0, -1):
        lower_cost = price / (meals_eaten * lower_weeks)
        upper_cost = price / (meals_eaten * upper_weeks)
        meal_costs.append({
            "Meals Eaten Per Week": meals_eaten,
            "Cost Per Meal (Range)": f"${round(upper_cost, 2)} - ${round(lower_cost, 2)}"
        })
    
    return meal_costs

def display_meal_costs(meal_costs):
    print(f"\n{'Meals Eaten Per Week':<25}{'Cost Per Meal (Range)':<25}")
    print("-" * 50)
    for entry in meal_costs:
        print(f"{entry['Meals Eaten Per Week']:<25}{entry['Cost Per Meal (Range)']:<25}")

# User input
def main():
    print("Welcome to the Meal Plan Calculator!")
    
    start_date = input("Enter the start date of the semester (YYYY-MM-DD): ")
    end_date = input("Enter the end date of the semester (YYYY-MM-DD): ")
    
    # Calculate and display days and weeks between start and end dates
    total_days, total_weeks = calculate_weeks_and_days(start_date, end_date)
    print(f"\nTotal days between {start_date} and {end_date}: {total_days} days")
    print(f"Total weeks between {start_date} and {end_date}: {total_weeks} weeks")
    
    staying_thanksgiving = input("\nAre you staying over Thanksgiving break? (yes/no): ").lower() == 'yes'
    
    # Adjust for Thanksgiving and display new calculation
    if staying_thanksgiving:
        print("\nNo change in the number of weeks because you are staying over Thanksgiving break.")
    else:
        print(f"\nThanksgiving break reduces the number of weeks by 1.")
        total_weeks -= 1
        print(f"Updated number of weeks: {total_weeks} weeks")
    
    # Calculate lower and upper bounds for the weeks
    lower_weeks = int(total_weeks)  # Lower bound (rounded down)
    upper_weeks = lower_weeks + 1   # Upper bound (rounded up)
    
    print("\nSelect a meal plan: ")
    for plan in meal_plans.keys():
        print(f"- {plan}")
    
    selected_plan = input("Enter the meal plan name: ")

    # Calculate meal costs using the range (lower and upper bounds)
    meal_costs = calculate_meal_costs_range(selected_plan, lower_weeks, upper_weeks)
    
    # Display the result
    print("\nMeal Plan Cost Breakdown")
    display_meal_costs(meal_costs)

if __name__ == "__main__":
    main()
