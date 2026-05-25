# Data Model

## Company

Represents an organization whose ESG data is being processed.

Fields:
- name

---

## DataSource

Represents uploaded CSV source information.

Fields:
- company
- source_type
- file_name
- uploaded_at

Supported sources:
- SAP
- UTILITY
- TRAVEL

---

## EmissionRecord

Represents normalized ESG activity records.

Fields:
- company
- source
- scope
- category
- activity_type
- raw_value
- raw_unit
- normalized_value
- normalized_unit
- occurred_at
- status
- is_suspicious
- created_at

Scopes:
- Scope 1
- Scope 2
- Scope 3

---

## AuditLog

Tracks changes made to emission records.

Fields:
- emission_record
- field_name
- old_value
- new_value
- changed_at