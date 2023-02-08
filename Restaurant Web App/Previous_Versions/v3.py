# Menu Dictonary with Prices
MENU_DICT = {'Cheese Burger': 3.23, 'Salad': 4.21, 'Steak': 14.12, 'Ribs': 16.12, 'Lasagna': 9.20,
             'Grilled Cheese': 4.20, 'Porkchop': 13.50, 'Mac and Cheese': 5.92, 'Pulled Pork': 5.23}

# Menu UI for Waitress/Waitor
menu_string = "1. Cheese Burger $3.23 2. Salad: $4.21 3. Steak: $14.12 4. Ribs $16.12 5. Lasagna: " \
              "$9.20 6. Grilled Cheese: $4.20 7. Porkchop $13.50 8. Mac and Cheese $5.92 9. Pulled Pork: $5.23 "
# Subtotal variable
subtotal = 0.0


# Calculator
def order_input():
    order_dict = {}
    global subtotal
    while True:
        print(menu_string)
        print("Please put in the customers order? ")
        order = input()
        if order in MENU_DICT:
            order_dict[order] = [MENU_DICT[order]]
            subtotal = subtotal + MENU_DICT[order]
        else:
            print("Incorrect input, please enter the customers order again")
            continue

        # This is why it double prints because we are returning order_dict every timne we add a new order so we need
        # to find a work around
        if completion():
            return order_dict


# Makes sure the calculator is finished, NEEDS WORK (SEE ABOVE COMMENT)
def completion():
    print("Would you like to add anything else? Yes/No")
    choice = input()
    if choice == "Yes":
        return False
    elif choice == "No":
        return True
    else:
        print("Invalid Input")


# Reciept for Customer
def receipt(order_list):
    for order in order_list:
        print(order)
        print("Total Price is: $", round(subtotal, 2))


# Allows the customer to put in multiple orders so they do not have to continue rerunning the program just to put in an order

def newOrder():
    print("")
    print("")
    print("")

    nOrder = input(print("Would you like to enter a new tables order?"))
    if nOrder == "Y" or "Yes":
        main()
    elif nOrder == "No" or "N":
        print("Ending Order")
        quit
    else:
        print("Please try again incorrect input")
        nOrder()


# designed to store the tables order and will be eventually added in as a prompt for the user
# to ask whether-or-not they want to see "Table order, or Input a order"
# creates a dictonary that can be rewritten based on if a new order comes in for the same table
# def tableStorage(table_number):
    # wip
def main():
    order = order_input()

    table_number = input("What is your table number? ")
    print("Your reciept for table number: ", table_number)
    receipt(order)

    newOrder()


if __name__ == "__main__":
    main()
