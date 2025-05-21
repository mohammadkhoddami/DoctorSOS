from .base import *
from .database import get_config_database


SECRET_KEY = 'django-insecure-ke4n56j!bs!saiesr@207_ly#jpk&3v2#k_91$x$0@fp5y_(^9'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = get_config_database()