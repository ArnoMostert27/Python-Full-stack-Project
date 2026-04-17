import os
import sys
from pathlib import Path

# This adds the folder containing 'config' to the path
# If your structure is: luxury_project/api/index.py
# Then Path(__file__).resolve().parent.parent is 'luxury_project'
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Fallback: manually check if we need to go deeper
if not os.path.exists(os.path.join(str(BASE_DIR), "config")):
    sys.path.append(os.path.join(str(BASE_DIR), "luxury_project"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()