import os
import sys
from pathlib import Path

# 1. Point to the folder containing 'manage.py'
# Current file is at /luxury_project/api/index.py
# .parent is /luxury_project/api/
# .parent.parent is /luxury_project/
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# 2. Correct the path to settings
# It is inside the 'config' folder which is inside 'luxury_project'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application

# Vercel looks for 'app'
app = get_wsgi_application()