# Tradeoffs

## SQLite Instead of PostgreSQL

SQLite was chosen for simplicity and faster local setup.

Tradeoff:
- limited scalability
- not ideal for concurrent production workloads

---

## Simplified Emission Calculations

The system currently stores normalized activity data without real emission factor calculations.

Tradeoff:
- simpler implementation
- less ESG calculation accuracy

---

## Static Date for Travel Data

Travel sample data did not contain dates.

A placeholder date was used for ingestion.

Tradeoff:
- simplified ingestion
- reduced temporal accuracy

---

## Minimal Frontend Styling

Focus was placed on backend ingestion logic rather than UI design.

Tradeoff:
- functional interface
- minimal visual polish