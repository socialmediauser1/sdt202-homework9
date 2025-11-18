# Costume Constructor (Alpha)

FastAPI web application that lets stylists and students catalog garments while laying the groundwork for the future outfit builder. The alpha milestone covers a PostgreSQL-backed wardrobe catalog with list/detail views and HTML forms with validation.

## Requirements

- Python 3.11+
- PostgreSQL 14+ (or compatible managed instance)

## Getting Started

1. **Clone & create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure the database connection**

   Set `DATABASE_URL` or create a `.env` file in the project root:
   ```
   DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/costume_constructor
   ```

   Create the database if it does not exist:
   ```bash
   createdb costume_constructor
   ```

3. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

   Visit `http://127.0.0.1:8000` for the landing page, `http://127.0.0.1:8000/clothes` for the catalog.

## Features in this Milestone

- SQLAlchemy models that map the milestone entities (Users, Clothes, Outfits, Outfit Items).
- CRUD flow for clothing pieces with server-side validation powered by Pydantic and clean flash-style error messaging.
- List/detail/form templates rendered with Jinja2 and styled with a lightweight CSS theme for readability.
- Navigation between the landing page, catalog, and creation workflows.
- Automatic table creation on startup to make the demo easy to run locally.

## Next Steps

- Build session-backed user accounts with login/register forms.
- Expand the Outfit builder canvas so saved clothes can be dragged onto looks.
- Add an admin dashboard for moderating users and bulk editing catalog entries.

