# My Django Projects

A small, conventional Django starter project. It includes a `core` app, a home page, template inheritance, static CSS, and environment-based settings.

## Get started

```bash
cd My_Django_Projects
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Create an admin user with `python manage.py createsuperuser`.

For deployment, set `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS` as environment variables.
