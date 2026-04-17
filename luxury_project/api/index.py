import os
import sys
from pathlib import Path

# Add the 'luxury_project' folder to the Python path
# This allows the app to find 'config', 'users', and 'vehicles'
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Tell Django where the settings file is located
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application

# Vercel needs 'app' to be defined
app = get_wsgi_application()