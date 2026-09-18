# Django REST API – Blog Post Management

This project is a small REST API assignment built with Django REST Framework. A signed-in user can create, read, update, and delete only their own blog posts.

## Setup

```bash
cd DjangoRestAPI-AregalaSaiCharithRoyal
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/api-auth/login/` to sign in through the DRF browsable API. The admin page is available at `/admin/` after creating a superuser.

## API endpoint

`/api/posts/`

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/posts/` | Lists only the logged-in user's posts (5 per page) |
| POST | `/api/posts/` | Creates a post; the author is set automatically |
| GET | `/api/posts/<id>/` | Reads one of the logged-in user's posts |
| PUT/PATCH | `/api/posts/<id>/` | Updates one of the logged-in user's posts |
| DELETE | `/api/posts/<id>/` | Deletes one of the logged-in user's posts |

Useful query parameters:

* `?created_at=2026-08-29` filters by creation date.
* `?search=django` searches both title and content.
* `?ordering=-id` orders newest IDs first (`id` and `-id` are supported).
* `?page=2` requests another page of results.

The API uses session authentication. Browsable API requests require login; unauthenticated API requests receive a JSON `401` response.

## Run tests

```bash
python manage.py test
```
