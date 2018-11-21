import os

# loaded from .env file in index.wsgi
def get_env(env_name):
    try:
        return os.environ[env_name]
    except KeyError:
        msg = "Variable '{}' not found".format(env_name)
        raise Exception(msg)
