import os
import sys
from pathlib import Path

# --- VITAL PATHING LOGIC ---
# This tells Vercel to look one level up so it can find 'config' and 'users'
current_path = Path(__file__).resolve()
base_dir = current_path.parent.parent
sys.path.append(str(base_dir))

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model

# Initialize the Django application
app = get_wsgi_application()

# --- AUTO-CREATE SUPERUSER ---
def create_superuser():
    User = get_user_model()
    # Pulls the credentials you saved in the Vercel Dashboard
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

    if username and password:
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser {username}...")
            User.objects.create_superuser(username=username, email=email, password=password)
        else:
            print(f"Superuser {username} already exists.")

# Run the check every time the function 'wakes up'
try:
    create_superuser()
except Exception as e:
    print(f"Superuser creation failed: {e}")