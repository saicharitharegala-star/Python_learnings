# Database Operations Example (test.py)

## Description
A minimal Python script demonstrating basic PostgreSQL operations using `psycopg2`.

The script (`test.py`) includes three functions:
- `table()` — creates an `employees` table (name, ID, age).
- `data()` — prompts for `name`, `ID`, and `age` and inserts a row.
- `extract()` — selects and prints all rows from the `employees` table.

Note: `test.py` calls `data()` and `extract()` when run. `table()` is defined but not invoked by default.

## Prerequisites
- Python 3.8+ (or any supported 3.x)
- PostgreSQL server running and accessible
- `psycopg2` Python package

Install the Python dependency:

```bash
pip install psycopg2-binary
```

## Configuration
The script currently contains hard-coded connection values (host, port, user, password, dbname). For safety, replace these with environment variables or a configuration file.

Example environment variables (bash/zsh):

```bash
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=postgres
export PGUSER=postgres
export PGPASSWORD=your_password_here
```

Tip: Update `test.py` to read these values from `os.environ` instead of hard-coded strings.

## Usage
1. Ensure PostgreSQL is running and reachable using the configured credentials.
2. (Optional) Create the table by calling `table()` from a Python REPL or modifying the script to invoke it.
3. Run the script to insert a row and show all rows:

```bash
python3 test.py
```

The script will prompt for `name`, `ID`, and `age`, insert the row, then print all rows.

## Security & Improvements
- Do NOT commit credentials to version control. Use environment variables or a secrets manager.
- Add error handling around database operations (try/except) and ensure connections/cursors are closed in `finally` blocks.
- Use parameterized queries (already used) and validate user input before inserting.
- Consider using connection pooling for production.

## Author
Created alongside `test.py`.
