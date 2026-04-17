import os
import sys
from pathlib import Path
from django.core.management import call_command # Add this import

# Absolute search for the project root
current_path = Path(__file__).resolve()
base_dir = None

for parent in current_path.parents:
    if (parent / 'manage.py').exists():
        base_dir = parent
        break

if base_dir:
    sys.path.append(str(base_dir))
    os.chdir(str(base_dir)) 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()

# --- ADD THESE TWO LINES ---
# This forces the database to create the 'vehicles_vehicle' table
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration failed: {e}")
# ---------------------------