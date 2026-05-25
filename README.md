# 🌱 Breathe ESG Assignment

A full-stack ESG data ingestion platform built using **Django REST Framework** and **React**.

---

# 📖 Overview

This project simulates a simplified ESG (Environmental, Social, and Governance) ingestion pipeline capable of processing data from multiple enterprise sources.

The platform accepts CSV uploads from different systems, normalizes the data, detects suspicious records, and stores everything in a centralized database.

Supported data sources include:

* SAP fuel data
* Utility electricity consumption data
* Business travel data

---

# ✨ Features

## 🔧 Backend

* Django REST Framework API
* CSV upload endpoint
* Dynamic schema detection
* Multi-source ingestion pipeline
* Data normalization
* Suspicious value detection
* SQLite database integration
* Django admin dashboard

## 🎨 Frontend

* React upload interface
* File selection and upload
* Axios-based API integration
* Upload success feedback

---

# 📂 Supported Data Sources

## ⛽ SAP Fuel Data

Example columns:

```text
FuelType, Quantity, Unit, Date
```

Processed as:

* Scope 1 emissions
* Fuel consumption activities

---

## ⚡ Utility Data

Example columns:

```text
MeterID, BillingStart, BillingEnd, kWh, Tariff
```

Processed as:

* Scope 2 emissions
* Electricity usage activities

---

## ✈️ Travel Data

Example columns:

```text
Employee, TravelType, FromCode, ToCode, Class, DistanceKm
```

Processed as:

* Scope 3 emissions
* Business travel activities

---

# 🛠️ Tech Stack

## Backend

* Python
* Django
* Django REST Framework
* Pandas
* SQLite

## Frontend

* React
* Axios

---

# 🧱 Project Structure

```text
breathe-esg-assignment/
│
├── backend/
│   ├── config/
│   ├── emissions/
│   ├── manage.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│
├── Sample_data/
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

## 1. Navigate to Backend

```bash
cd backend
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run Database Migrations

```bash
python manage.py migrate
```

## 6. Start Backend Server

```bash
python manage.py runserver
```

Backend runs at:

```text
http://127.0.0.1:8000/
```

---

# 💻 Frontend Setup

## 1. Navigate to Frontend

```bash
cd frontend
```

## 2. Install Dependencies

```bash
npm install
```

## 3. Start Frontend

```bash
npm start
```

Frontend runs at:

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

Django admin is available at:

```text
http://127.0.0.1:8000/admin/
```

---

# 🚀 Deployment

## Frontend Deployment

Frontend can be deployed using:

* Vercel
* Netlify

## Backend Deployment

Backend can be deployed using:

* Render
* Railway
* PythonAnywhere

---

# 🌐 Deployment URLs

## Frontend

```text
Add your deployed frontend URL here
```

## Backend API

```text
Add your deployed backend URL here
```

---

# 📄 Requirements File

Create a `requirements.txt` file inside the `backend/` folder with:

```text
django
djangorestframework
pandas
django-cors-headers
```

Generate automatically using:

```bash
pip freeze > requirements.txt
```

---

# 🚀 Future Improvements

* PostgreSQL integration
* Authentication and authorization
* Advanced ESG calculations
* Dashboard analytics
* Cloud deployment
* Improved UI/UX

---

# 👨‍💻 Author

Kuruva Rajeshwari
