"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45

PS5_PRICE = 631.945
# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (CLASS_DAYS_PER_SEMESTER*2)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost)/credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (cost_per_credit(annual_cost, credits)*CS1430_CREDITS)/CS1430_MEETINGS_PER_SEMESTER


def cost_per_ps5(annual_cost):
    """Give back how many PS5s you could buy (with tax)."""
    return annual_cost / PS5_PRICE


def cost(i):
    if i==1:
        return "Cost per semester"
    elif i==2:
        return "Cost per month"
    elif i==3:
        return "Cost per day"
    elif i==4:
        return "Cost per credit"
    elif i==5:
        return "Cost per CS1430 class"
    elif i==6:
        return "How many PS5s"

# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost=float(input("What is the total cost for one year? "))
    credits=int(input("What is the amount of credits this semester? "))
    
    while True:
        # Show your menu here.
        for i in range (1,7):
            print(str(i)+":", cost(i))
        print("Q")
        choice = input("Choose an option: ")
        if choice=="1":
            semester=cost_per_semester(annual_cost)
            print(f"One semester costs ${semester:,.2f}")
        if choice=="2":
            month=cost_per_month(annual_cost)
            print(f"One month costs ${month:,.2f}")
        if choice=="3":
            day=cost_per_day(annual_cost)
            print(f"One day costs ${day:,.2f}")
        if choice=="4":
            credit=cost_per_credit(annual_cost, credits)
            print(f"One credit costs ${credit:,.2f}")
        if choice=="5":
            CS1430_class=cost_per_class(annual_cost, credits)
            print(f"One CS1430 class costs ${CS1430_class:,.2f}")
        if choice=="6":
            ps5=cost_per_ps5(annual_cost)
            if ps5>=2 or ps5<1:
                print("You could buy", int(ps5//1), "PS5s")
            else:
                print("You could buy", int(ps5//1), "PS5")
        if choice == "Q":
            break

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
