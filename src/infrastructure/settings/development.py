from pathlib import Path
from src.infrastructure.settings.base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusion_server',
        'USER': 'fusion_auth_user',
        'PASSWORD': 'fusion_auth_password',
        'HOST': 'server-postgres-srv',
        'PORT': '5432',
    }
}