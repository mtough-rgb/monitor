# Project Requirements

This project is a small Python-based EDI monitor built with Flask and SQLite.

## Runtime Requirements

- Python 3.10 or newer
- `pip` for Python package installation
- SQLite support

Note: `sqlite3` is used by the project but does not need a separate install in a standard Python distribution because it is part of the Python standard library.

## Python Modules Used

### External package

- `Flask`

### Standard library modules

- `sqlite3`

## Install Steps

From `C:\Projects\Monitor`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install Flask
```

## Project Files and What They Need

- `app.py`
  - Requires: `Flask`, `sqlite3`
  - Purpose: runs the web dashboard
- `init_db.py`
  - Requires: `sqlite3`
  - Purpose: creates the `edi_transactions` table in `monitor.db`
- `seed_test_data.py`
  - Requires: `sqlite3`
  - Purpose: inserts sample data
- `query_db.py`
  - Requires: `sqlite3`
  - Purpose: prints all rows from the database
- `view_data.py`
  - Requires: `sqlite3`
  - Purpose: displays all rows from the database
- `status_summary.py`
  - Requires: `sqlite3`
  - Purpose: prints grouped counts by status
- `templates/dashboard.html`
  - Requires: Flask template rendering
  - Purpose: dashboard UI

## Setup Order

Run these commands after installing dependencies:

```powershell
python init_db.py
python seed_test_data.py
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

## Optional Freeze File

If you want to capture the environment exactly, run:

```powershell
pip freeze > requirements.txt
```

At minimum, the project currently depends on:

```text
Flask
```
