from flask import Flask, render_template, request

app = Flask(__name__)
order_items = []
cost = 5

@app.route('/')
def home():
    return render_template("order-form.html")

@app.route('/transaction', methods=['POST'])
def compute():
    global balance
    table = request.form['table']
    order = request.form['order']


    content = {"table": table,
         "order": order,
         "cost" : cost,
         }

    order_items.append(content)
    return render_template("order-result.html",
                           content=order_items)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)