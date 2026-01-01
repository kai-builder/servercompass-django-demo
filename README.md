# ServerCompass Django Demo

A Django REST API demo project that exposes environment variables to the frontend.

## Features

- Django 6.0 REST API
- Environment variable management using python-decouple
- Public environment variables endpoint (only exposes NEXT_PUBLIC_* variables)
- Health check endpoint

## Project Structure

```
servercompass-django-demo/
├── config/                 # Django project settings
│   ├── settings.py        # Main settings (uses environment variables)
│   ├── urls.py            # URL routing
│   └── wsgi.py
├── api/                   # API app
│   ├── views.py           # API endpoints
│   └── urls.py            # API URL routing
├── .env                   # Environment variables (not committed to git)
├── requirements.txt       # Python dependencies
└── manage.py              # Django management script
```

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   The `.env` file contains all configuration. Update values as needed:
   ```env
   # Public variables (exposed to frontend)
   NEXT_PUBLIC_APP_NAME=ServerCompass Demo
   NEXT_PUBLIC_API_URL=https://api.servercompass.app
   NEXT_PUBLIC_ENVIRONMENT=production
   NEXT_PUBLIC_VERSION=1.0.0

   # Private variables (never exposed)
   DATABASE_URL=postgresql://user:password@localhost:5432/servercompass
   API_SECRET_KEY=your-secret-key-here
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

## Pages & Endpoints

### Homepage
```
GET /
```

A beautiful web interface displaying all public environment variables (`NEXT_PUBLIC_*`) with links to API endpoints.

### Get Public Environment Variables
```
GET /api/env/
```

Returns only environment variables prefixed with `NEXT_PUBLIC_*` for safe frontend consumption.

**Response:**
```json
{
  "NEXT_PUBLIC_APP_NAME": "ServerCompass Demo",
  "NEXT_PUBLIC_API_URL": "https://api.servercompass.app",
  "NEXT_PUBLIC_ENVIRONMENT": "production",
  "NEXT_PUBLIC_VERSION": "1.0.0"
}
```

### Health Check
```
GET /api/health/
```

**Response:**
```json
{
  "status": "ok",
  "message": "Server Compass API is running"
}
```

## Testing

View the homepage in your browser:

```
http://localhost:8000/
```

Or test the endpoints using curl:

```bash
# Homepage HTML
curl http://localhost:8000/

# Get public environment variables (JSON)
curl http://localhost:8000/api/env/

# Health check
curl http://localhost:8000/api/health/
```

## Security Notes

- Only variables prefixed with `NEXT_PUBLIC_*` are exposed via the API
- Private variables (DATABASE_URL, API_SECRET_KEY, etc.) are never exposed
- The `.env` file should never be committed to version control
- Add `.env` to your `.gitignore` file

## Dependencies

- Django 6.0
- python-decouple 3.8
