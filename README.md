# 🏦 Bank Branch API (Flask + SQLite)

A simple Flask-based RESTful API and Web App that allows users to:

- View a list of banks.
- Search for branch details by IFSC code.
- Display results in a clean, table-based web format.

---

## 💡 Features

- Built with **Flask** and **SQLAlchemy**.
- SQLite database support.
- Clean separation of **API data** and **HTML rendering**.
- Responsive, easy-to-navigate front-end using plain HTML & CSS.
- Deployable on platforms like **PythonAnywhere**.

---

## ⚙️ Tech Stack

- Python 3
- Flask
- SQLAlchemy (ORM)
- SQLite
- HTML / CSS

---

## 🚀 How to Run Locally

1️⃣ Clone the repository:
```bash
git clone https://github.com/IIUday/BankVault.git
cd BankVault
```

2️⃣  Create and activate virtual environment:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```
`

3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```
Create a `bank.db` SQLite database and add `bank_branches`  table or use the database file given in the Tests folder.
 
4️⃣ Run the server:
```bash
python app/server.py
```

Visit:  
```
http://127.0.0.1:5000/
```

---

## 🌐 API Endpoints

| Method | URL                       | Description                      |
|--------|---------------------------|----------------------------------|
| `GET`  | `/banks`                  | Returns a list of all banks.     |
| `GET`  | `/branches/<ifsc>`        | Returns details of a specific branch by IFSC code. |

---

## 💻 Web Pages

- `/` — Home page with buttons for bank list and IFSC search.
- `/banks` — Displays the complete bank list in table format.
- `/branches/<ifsc>` — Displays the branch details in table format.

---

## 📦 Deployment Guide

You can easily deploy this app on:

- [PythonAnywhere](https://www.pythonanywhere.com/)
- [Heroku](https://www.heroku.com/)
- [Render](https://render.com/)

For **PythonAnywhere**:

1. Upload your project via the file manager.
2. Configure `WSGI` to point to your `server.py`.
3. Set up your virtual environment and install dependencies.
4. Restart your web app!

---

## 📜 License

MIT License. Free to use and distribute!

---

