
menu: dict[str, float]= {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    """
    User can order items off the menu one at a time.
    Each correctly inputted item is totaled to their 'bill'.
    [CTRL + D] {EOFError} to end their order.
    """

    bill = 0

    while True:
        try:
            # Input stored and formatted to match dict
            user_order = input("Item: ").title()
            if user_order in menu:
                # Add's value to bill
                bill += menu[user_order]
                # Displays bill after proper input
                print(f"Total: ${bill:.2f}")

        except EOFError:
            # New line for bash
            print()
            break
        except EOFError:
            pass

if __name__ == "__main__":
     main()
