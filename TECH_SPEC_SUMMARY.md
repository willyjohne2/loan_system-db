# Loan System API - Technical Project Summary

This document summarizes the current state of the project as of February 5, 2026. Keep this file for reference when moving to a new workspace.

## 1. Project Links & Credentials

- **Live API:** [https://loan-system-api-0knv.onrender.com](https://loan-system-api-0knv.onrender.com)
- **GitHub Repository:** [https://github.com/willyjohne2/loan_system-db.git](https://github.com/willyjohne2/loan_system-db.git)
- **Database Connection String (PostgreSQL):**
  `postgresql://loan_sytem_db_user:QqPUj19561h5nMkUFuGRwwkyzAdamUnI@dpg-d61eo14r85hc7399gmu0-a.oregon-postgres.render.com/loan_sytem_db`
- **Super Admin Credentials:**
  - Email: `njugunawilson977@gmail.com`
  - Password: `27580072@willy`

## 2. Key Architecture Details

- **Framework:** Django 6.0.2 + Django REST Framework 3.16.1.
- **Authentication:** Custom JWT implemented via `SimpleJWT`.
- **Hosting:** Render (Web Service + PostgreSQL Instance).
- **Security:** Use of `.env` files for secrets; `CORS_ALLOW_ALL_ORIGINS` enabled for integration.

## 3. Important Files in GitHub

- `INTEGRATION_GUIDE.md`: Contains Express.js code examples and connection steps for the other team.
- `database_schema.sql`: Full SQL export of the database tables.
- `apps/models.py`: The "Source of Truth" for all user, loan, and repayment data structures.
- `render.yaml`: Configuration for the cloud deployment.

## 4. Current Working State

- The API is **Live and Verified**.
- The `LoginView` has been modified to handle the "Browsable API" content wrapper.
- All database tables are marked as `managed = True` in Django.

## 5. Next Steps for Handoff

1. Share the GitHub URL with the Express team.
2. Point them specifically to `INTEGRATION_GUIDE.md`.
3. If they encounter issues with JWT tokens, verify they are using the correct `Authorization: Bearer <token>` header.
