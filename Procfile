release: python manage.py migrate
web: uvicorn william.asgi:application --port $PORT --host 0.0.0.0
