import os

def current_env():
    try:
        from flask import current_app
        if current_app.config.get('TESTING'):
            return 'test'
    except RuntimeError:
        pass

    now = os.getenv("ENV", None)
    if now == None:
        return 'development'
    else:
        return now

if current_env() == 'test':
    from config.environments.test import EnvironmentTest as env
else:
    from config.environments.development import EnvironmentDevelopment as env
