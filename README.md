# 🌸 GlowCare – Skincare E-commerce Website

GlowCare is a simple and vibrant **skincare e-commerce web application** built using **Flask (Python)**.
It allows users to browse skincare products, add them to a cart, and simulate a checkout process.

---

## 🚀 Features

* 🧴 View skincare products (Face Wash, Serum, Sunscreen, etc.)
* ➕ Add products to cart
* 🛒 View cart with total price
* ❌ Remove items (optional enhancement)
* ✅ Checkout functionality
* 🎨 Colorful and vibrant UI

---

## 🛠️ Technologies Used

* **Backend:** Python with Flask
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Session Handling:** Flask sessions (for cart storage)

---

## 📁 Project Structure

```id="jrvp4g"
GlowCare/
│── app.py
│── database.db
│
│── templates/
│   ├── index.html
│   ├── cart.html
│   ├── checkout.html
│
│── static/
│   ├── style.css
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```id="s62s86"
git clone https://github.com/your-username/glowcare.git
cd glowcare
```

2. Install dependencies:

```id="c9j1q3"
pip install flask
```

3. Run the application:

```id="g9n5fc"
python app.py
```

4. Open in browser:

```id="1t0g7p"
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

* Products are stored in an SQLite database
* Flask handles routing and backend logic
* Product data is displayed using Jinja templates
* Cart data is stored temporarily using sessions
* Total price is calculated dynamically

---

## 📌 Key Functionalities

* **Home Page:** Displays all skincare products
* **Add to Cart:** Stores product IDs in session
* **Cart Page:** Fetches products from database and calculates total
* **Checkout:** Clears cart and shows confirmation

---

## ⚠️ Limitations

* No user authentication
* No real payment gateway
* Cart resets when server restarts
* Uses static product data

---

## 🚀 Future Improvements

* 🔍 Search and filter products
* 🧴 Product categories (Cleanser, Serum, Sunscreen)
* 🔐 User login/signup system
* 💳 Payment integration
* ☁️ Cloud database

---

## 👩‍💻 Author

Srishti Setia

---

## 📄 License

This project is open-source and available under the MIT License.
