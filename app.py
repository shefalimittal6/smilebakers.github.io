from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Chocolate Cake", "price": "₹600", "image": "chocolate_cake.jpeg"},
    {"id": 2, "name": "Vanilla Cake", "price": "₹500", "image": "vanilla_cake.jpg"},
    {"id": 3, "name": "Strawberry Cake", "price": "₹550", "image": "strawberry_cake.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
