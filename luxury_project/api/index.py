import os
import sys
from pathlib import Path

# Add the 'luxury_project' folder to the Python path
# Current file: /luxury_project/api/index.py -> .parent.parent is /luxury_project/
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Explicitly point to the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application

# Vercel searches for 'app'
app = get_wsgi_application()