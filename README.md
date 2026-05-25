# 🌱 Breathe ESG Assignment

A full-stack ESG data ingestion platform built using Django REST Framework and React.

---

# 📖 Overview

This project simulates a simplified ESG (Environmental, Social, and Governance) ingestion pipeline capable of processing data from multiple enterprise sources.

The platform accepts CSV uploads from different systems, normalizes the data, detects suspicious records, and stores everything in a centralized database.

The application supports:

- SAP fuel data
- Utility electricity consumption data
- Business travel data

---

# ✨ Features

## 🔧 Backend

- Django REST Framework API
- CSV upload endpoint
- Dynamic schema detection
- Multi-source ingestion pipeline
- Data normalization
- Suspicious value detection
- SQLite database integration
- Django admin dashboard

## 🎨 Frontend

- React upload interface
- File selection and upload
- API integration using Axios
- Upload success feedback

---

# 📂 Supported Data Sources

## ⛽ SAP Fuel Data

Example columns:

```text
FuelType, Quantity, Unit, Date
```

Processed as:

- Scope 1 emissions
- Fuel consumption activities

---

## ⚡ Utility Data

Example columns:

```text
MeterID, BillingStart, BillingEnd, kWh, Tariff
```

Processed as:

- Scope 2 emissions
- Electricity usage activities

---

## ✈️ Travel Data

Example columns:

```text
Employee, TravelType, FromCode, ToCode, Class, DistanceKm
```

Processed as:

- Scope 3 emissions
- Business travel activities

---

# 🛠️ Tech Stack

## Backend

- Python
- Django
- Django REST Framework
- Pandas
- SQLite

## Frontend

- React
- Axios

---

# 🧱 Project Structure

```text
breathe-esg-assignment/
│
├── backend/
│   ├── config/
│   ├── emissions/
│   ├── manage.py
│   └── venv/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── sample_data/
│   ├── sap/
│   ├── utility/
│   └── travel/
│
├── docs/
│   ├── MODEL.md
│   ├── DECISIONS.md
│   ├── TRADEOFFS.md
│   └── SOURCES.md
│
└── README.md
```

---

# ⚙️ Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install django djangorestframework pandas django-cors-headers

python manage.py migrate

python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000/
```

---

# 💻 Frontend Setup

```bash
cd frontend

npm install

npm install axios

npm start
```

Frontend URL:

```text
http://localhost:3000/
```

---

# 🔌 API Endpoint

## Upload CSV

```http
POST /api/upload/
```

Form Data:

```text
file = csv_file
```

---

# 🔄 Application Workflow

```text
CSV Upload
    ↓
Schema Detection
    ↓
Normalization
    ↓
Suspicious Data Detection
    ↓
Database Storage
```

---

# 🗄️ Admin Panel

Django admin can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

---

# 🚀 Future Improvements

- PostgreSQL integration
- Authentication and authorization
- Advanced ESG calculations
- Dashboard analytics
- Cloud deployment
- Better UI/UX

---

# 👨‍💻 Author

Rajeshwari

