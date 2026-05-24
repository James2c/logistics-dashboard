# 📦 Procurement Analytics Dashboard

A full-stack logistics and procurement analytics platform built with Python, FastAPI, Streamlit, SQLAlchemy, and SQLite.

This project simulates a lightweight ERP-style procurement system with:
- Vendor management
- Purchase order tracking
- Inventory monitoring
- Low-stock alerts
- Interactive analytics dashboards
- KPI reporting

---

# 🚀 Features

## Backend API (FastAPI)
- RESTful API architecture
- Vendor management endpoints
- Purchase order management
- Inventory tracking
- SQLAlchemy ORM integration
- Pydantic validation schemas

## Dashboard (Streamlit)
- Interactive procurement dashboard
- KPI cards
- Analytics charts
- Inventory intelligence
- Purchase order analytics
- Low-stock alert system

## Data & Analytics
- Inventory valuation
- Reorder point monitoring
- Purchase order status tracking
- Vendor performance visualization
- Realistic seeded business data

---

# 🛠 Tech Stack

| Technology | Purpose |

| Python | Core programming language |
| FastAPI | Backend REST API |
| Streamlit | Dashboard frontend |
| SQLAlchemy | ORM / database layer |
| SQLite | Relational database |
| Pandas | Data analysis |
| Plotly | Interactive charts |
| Git & GitHub | Version control |

---

# 📂 Project Structure

```text
logistics-dashboard/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── scripts/
│   └── seed_data.py
│
├── data/
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/James2c/logistics-dashboard.git
cd logistics-dashboard
```

---

## 2. Create Virtual Environment

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🌱 Seed Dummy Data

Populate the database with realistic procurement and inventory data:

```bash
python -m scripts.seed_data
```

---

# ▶️ Running the Application

## Start Backend API

```bash
uvicorn app.main:app --reload
```

API Documentation:
```text
http://127.0.0.1:8000/docs
```

---

## Start Dashboard

Open a second terminal:

```bash
streamlit run dashboard/app.py
```

Dashboard URL:
```text
http://localhost:8501
```

---

# 📊 Dashboard Features

- Procurement KPI tracking
- Inventory analytics
- Low-stock alerts
- Purchase order visualization
- Inventory valuation charts
- Status filtering
- Interactive data tables

---

# 🔮 Future Improvements

- User authentication
- PostgreSQL integration
- Docker deployment
- CI/CD pipeline
- Cloud deployment
- AI-powered analytics insights
- Supplier scorecards

---


# 🧠 What I Learned

This project helped strengthen skills in:
- Backend API development
- Database design
- Full-stack architecture
- Data visualization
- Business analytics workflows
- Python project organization
- Git & GitHub workflows

---

# 📄 License

This project is licensed under the MIT License.