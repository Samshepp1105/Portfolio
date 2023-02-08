from flask import Flask, render_template, request

app = Flask(__name__)
order_items = []

# Menu Dictionary with Prices
MENU_DICT = {'Cheese Burger': 3.23, 'Salad': 4.21, 'Steak': 14.12, 'Ribs': 16.12, 'Lasagna': 9.20,
             'Grilled Cheese': 4.20, 'Porkchop': 13.50, 'Mac and Cheese': 5.92, 'Pulled Pork': 5.23}

# Menu UI for Waitress/Waiter
menu_string = "1. Cheese Burger $3.23 2. Salad: $4.21 3. Steak: $14.12 4. Ribs $16.12 5. Lasagna: " \
              "$9.20 6. Grilled Cheese: $4.20 7. Porkchop $13.50 8. Mac and Cheese $5.92 9. Pulled Pork: $5.23 "
i = 0
cost = 0

@app.route('/')
def home():
    return render_template("order-form.html")


@app.route('/transaction', methods=['POST'])
def compute():
    global gorder
    global gtable
    table = request.form['table']
    rqorder = request.form['order']
    order = rqorder.split()
    cost = calculation(order)
    content = {"table": table,
               "order": rqorder,
               "cost": cost,
               }

    order_items.append(content)
    return render_template("order-result.html",
                           content=order_items)

def calculation(order):
    cost = 0
    for i in order:
        print(i)
        if i in MENU_DICT:
            cost = cost + MENU_DICT[i]
            print(MENU_DICT[i])

    return round(cost, 2)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)