

MENU_DICT = {'Cheese Burger': 3.23, 'Salad' : 4.21, 'Steak' : 14.12,'Ribs' : 16.12, 'Lasagna' : 9.20, 'Grilled Cheese' : 4.20, 'Porkchop' : 13.50, 'Mac and Cheese' : 5.92, 'Pulled Pork' : 5.23}

menu_string = "1. Cheese Burger $3.23 2. Salad: $4.21 3. Steak: $14.12 4. Ribs $16.12 5. Lasagna: " \
              "$9.20 6. Grilled Cheese: $4.20 7. Porkchop $13.50 8. Mac and Cheese $5.92 9. Pulled Pork: $5.23 "
subtotal = 0.0


def order_input():
    current_order = []
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
        if completion():
            return current_order, order_dict

def completion():
    print("Would you like to add anything else? Yes/No")
    choice = input()
    if choice == "Yes":
        return False
    elif choice == "No":
        return True
    else:
        print("Invalid Input")


def receipt(order_list):
    for order in order_list:
        print("Total Price is: $", order)


def main():
    order = order_input()
    table_number = input("What is your table number? ")
    print("Your reciept for table number: ", table_number)
    print(subtotal)
    receipt(order)


if __name__ == "__main__":
    main()