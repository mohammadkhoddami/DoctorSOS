import os
import environ

# Initialize environ
env = environ.Env(
    DJANGO_SETTINGS_MODULE=(str, 'config.settings.develop')
)

# Read .env file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
env.read_env(os.path.join(BASE_DIR, '.env'))

# Get the settings module from environment variable
DJANGO_SETTINGS_MODULE = env('DJANGO_SETTINGS_MODULE')

# Import the appropriate settings
if DJANGO_SETTINGS_MODULE == 'config.settings.develop':
    from .develop import *
elif DJANGO_SETTINGS_MODULE == 'config.settings.production':
    from .production import *
else:
    from .develop import *