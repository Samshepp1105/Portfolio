from flask import *

app = Flask(__name__)
order_items = []

# Menu Dictionary with Prices
MENU_DICT = {'Burger': 3.23, 'Salad': 4.21, 'Steak': 14.12, 'Ribs': 16.12, 'Lasagna': 9.20,
             'PB&J': 4.20, 'Porkchop': 13.50, 'Macaroni': 5.92, 'Meatloaf': 5.23}

# Menu UI for Waitress/Waiter
menu_string = "1.Burger $3.23 2. Salad: $4.21 3. Steak: $14.12 4. Ribs $16.12 5. Lasagna: " \
              "$9.20 6. PB&J: $4.20 7. Porkchop $13.50 8. Macaroni $5.92 9. Meatloaf: $5.23 "
table_string = " 1 2 3 4 5 6 7 8 9 10 11 12"
i = 0
cost = 0
global gorder
global gtable


@app.route('/error')
def error():
    return "<p><strong> Enter valid table number<strong><p>"


@app.route('/')
def home():
    return render_template("Table Select.html")


@app.route('/Order', methods=['GET', 'POST'])
def order():
    if request.method == "POST" or "GET":
        table_num = request.form['table']
    if table_num in table_string:
        resp = make_response(render_template('order-form.html'))
        resp.set_cookie('table_num', table_num)
        return resp,table_num
    else:
        return redirect(url_for('error'))




@app.route('/transaction', methods=['GET', 'POST'])
def compute():
    global gorder
    global gtable
    table = request.cookies.get('table_num')
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