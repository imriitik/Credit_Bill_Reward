# 🎁 BON Rewards – Bill Payment Reward System

A simple backend system built with **FastAPI + SQLite** that rewards users with gift cards when they pay their last 3 bills on time.  

---

## 🚀 Features
- User Management – Create and view users.  
- Bill Tracking – Add bills (with due date) for users.  
- Bill Payment – Pay bills and check timeliness.  
- Rewards – Automatically generate a reward if the last 3 bills were paid on time.  
- Database – Uses SQLite for persistence.  
- API Docs – Interactive API documentation via Swagger UI & Redoc.  
- DB Inspection Tool – Pretty-print tables (`users`, `bills`, `rewards`) using `tabulate`.  

---

## 📂 Project Structure
```

BON/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   └── show_db.py
│
├── bon_rewards.db
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup & Installation

```bash
# Clone repo
git clone <your-repo-url>
cd BON

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
````

Server runs at 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📖 API Endpoints

### Create User

```http
POST /users/
```

```json
{
  "name": "Ritik Kumar",
  "email": "ritik@example.com"
}
```

### Add Bill

```http
POST /bills/
```

```json
{
  "user_id": 1,
  "due_date": "2025-09-15"
}
```

### Pay Bill

```http
POST /bills/pay/{bill_id}
```

### Check Rewards

```http
GET /rewards/{user_id}
```

---

## 🛠️ DB Inspection

```bash
python app/show_db.py
```

Example output:

```
=== USERS ===
╒════╤═══════════════╤════════════════════════════╕
│ id │ name          │ email                      │
╞════╪═══════════════╪════════════════════════════╡
│ 1  │ Ritik Kumar   │ ritik@example.com          │
╘════╧═══════════════╧════════════════════════════╛
```

