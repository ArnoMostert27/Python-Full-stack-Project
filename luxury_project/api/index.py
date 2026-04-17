import os
import sys
from pathlib import Path

# Absolute search for the project root
current_path = Path(__file__).resolve()
base_dir = None

# Look upwards until we find 'manage.py' or 'config'
for parent in current_path.parents:
    if (parent / 'manage.py').exists() or (parent / 'config').exists():
        base_dir = parent
        break

if base_dir:
    sys.path.append(str(base_dir))
    # Add the specific config path as a backup
    sys.path.append(os.path.join(str(base_dir), "config"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()