import os
import sys
from pathlib import Path

# --- VITAL PATHING LOGIC ---
current_path = Path(__file__).resolve()
base_dir = current_path.parent.parent
sys.path.append(str(base_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model

app = get_wsgi_application()

# --- FORCED ADMIN REPAIR LOGIC ---
def create_superuser():
    User = get_user_model()
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')

    if username and password:
        # get_or_create handles both "new user" and "existing user"
        user, created = User.objects.get_or_create(username=username, defaults={'email': email})
        
        # We set these every time to make sure the account isn't "locked out"
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True  # This is the "Key" to the admin panel
        user.save()
        
        if created:
            print(f"✅ Created NEW superuser: {username}")
        else:
            print(f"🔄 Updated existing superuser: {username}")

try:
    create_superuser()
except Exception as e:
    print(f"Superuser repair failed: {e}")