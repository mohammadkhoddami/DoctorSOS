from .base import *




DATABASE_CONFIG = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT')
    }
}



def get_config_database(overrides=None):
    
    
    config = DATABASE_CONFIG.copy()
    
    if overrides:
        for db, params in overrides.items():
            if db in config:
                config[db].update(params)
            else:
                config[db] = params
                
    return config
