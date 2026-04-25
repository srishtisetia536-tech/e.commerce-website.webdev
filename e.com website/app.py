from flask import Flask, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS products
        (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, image TEXT)
    ''')

    c.execute("DELETE FROM products")

    products = [
    ("Face Wash", 299, "https://cdn.pixabay.com/photo/2017/08/06/01/45/soap-2580843_1280.jpg"),
    ("Sunscreen SPF 50", 499, "https://cdn.pixabay.com/photo/2016/11/29/05/08/cosmetics-1867207_1280.jpg"),
    ("Vitamin C Serum", 699, "https://cdn.pixabay.com/photo/2017/09/02/13/33/cosmetic-2701026_1280.jpg"),
    ("Moisturizer", 399, "https://cdn.pixabay.com/photo/2017/03/27/14/56/cream-2176784_1280.jpg"),
    ("Niacinamide Serum", 599, "https://cdn.pixabay.com/photo/2016/11/21/15/47/cosmetics-1843490_1280.jpg"),
    ("Aloe Vera Gel", 199, "https://cdn.pixabay.com/photo/2017/08/06/01/44/aloe-vera-2580842_1280.jpg")
]

    for i, p in enumerate(products, start=1):
        c.execute("INSERT INTO products VALUES (?, ?, ?, ?)", (i, p[0], p[1], p[2]))

    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    return render_template("index.html", products=products)

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(id)
    session.modified = True
    return redirect('/')

@app.route('/cart')
def cart():
    cart_ids = session.get('cart', [])
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    items = []
    total = 0

    for pid in cart_ids:
        c.execute("SELECT * FROM products WHERE id=?", (pid,))
        p = c.fetchone()
        if p:
            items.append(p)
            total += p[2]

    conn.close()
    return render_template("cart.html", items=items, total=total)

@app.route('/checkout')
def checkout():
    session['cart'] = []
    return render_template("checkout.html")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)