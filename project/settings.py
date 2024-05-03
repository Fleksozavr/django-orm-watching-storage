import os
from dotenv import load_dotenv


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.environ["ENGINE_DB"],
        'HOST': os.environ["HOST_DB"],
        'PORT': os.environ["PORT_DB"],
        'NAME': os.environ["NAME_DB"],
        'USER': os.environ["USER_DB"],
        'PASSWORD': os.environ["PASSWORD_DB"],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG_MODE = os.environ["DEBUG_MODE", ""]
debug_mode_lower = debug_mode.lower()
is_true = debug_mode_lower in ["true"]
DEBUG = not (not is_true)
    
ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.environ('ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
