import os
import sys
from pathlib import Path

# Absolute search for the project root
current_path = Path(__file__).resolve()
base_dir = None

# Look upwards until we find 'manage.py'
for parent in current_path.parents:
    if (parent / 'manage.py').exists():
        base_dir = parent
        break

if base_dir:
    sys.path.append(str(base_dir))
    # This ensures apps like 'users' and 'vehicles' are found
    os.chdir(str(base_dir)) 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()