# Costume Constructor - Alpha Version

A FastAPI application for managing clothing items and building outfits.

## Features (Alpha Version)

- ✅ CRUD operations for clothing items
- ✅ PostgreSQL database support (SQLite for development)
- ✅ Jinja2 templates with list, detail, and form views
- ✅ Server-side validation and error handling
- ✅ User-friendly navigation and styling

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Configuration

Create a `.env` file in the project root:

```env
# For PostgreSQL (recommended):
# Both formats work with psycopg3:
DATABASE_URL=postgresql://username:password@localhost:5432/costume_constructor
# or explicitly:
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/costume_constructor

# For SQLite (default, for development):
DATABASE_URL=sqlite:///./test.db
```

If no `.env` file is provided, the application defaults to SQLite (`sqlite:///./test.db`).

### 3. Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

### 4. Database Tables

Tables are automatically created on startup. The main entities are:
- `clothes` - Clothing items catalog
- `users` - User accounts (for future use)
- `outfits` - Outfit collections (for future use)
- `outfit_items` - Outfit-clothing relationships (for future use)

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database operations
│   └── routers/
│       ├── __init__.py
│       └── clothes.py    # Clothing routes
├── templates/            # Jinja2 templates
│   ├── base.html
│   ├── home.html
│   └── clothes/
│       ├── list.html
│       ├── detail.html
│       └── form.html
├── static/
│   └── styles.css        # CSS styles
└── requirements.txt      # Python dependencies
```

## Usage

1. **Home Page** (`/`) - Overview and navigation
2. **Clothing Catalog** (`/clothes`) - List all clothing items
3. **Add Garment** (`/clothes/new`) - Create a new clothing item
4. **View Details** (`/clothes/{id}`) - View clothing item details
5. **Edit Garment** (`/clothes/{id}/edit`) - Edit a clothing item
6. **Delete Garment** (`/clothes/{id}/delete`) - Delete a clothing item (POST)

## Validation

The application includes server-side validation:
- Name: 2-120 characters, required
- Category: Required, must be one of: top, bottom, shoes, accessory, outerwear
- Color: Optional, max 50 characters
- Size: Optional, max 40 characters
- Description: Optional, max 600 characters
- Image URL: Optional, must be a valid HTTP/HTTPS URL if provided

## Notes

This is an alpha version. Future features will include:
- User authentication
- Outfit creation and management
- Image upload functionality
- Advanced search and filtering

