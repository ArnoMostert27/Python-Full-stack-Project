import os
import sys
from pathlib import Path
from django.core.management import call_command

# ... (keep your existing sys.path and os.environ logic here) ...

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model

app = get_wsgi_application()

# --- AUTO-CREATE SUPERUSER FROM VERCEL ENV VARS ---
def create_superuser():
    User = get_user_model()
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if username and password:
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser {username}...")
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            print(f"Superuser {username} already exists.")

# Run the check
try:
    create_superuser()
except Exception as e:
    print(f"Superuser creation failed: {e}")