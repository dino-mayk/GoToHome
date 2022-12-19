import os
from os.path import dirname, join
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# dotenv_path = join(dirname(__file__), '.env')
dotenv_path = join(dirname(__file__), '../dev.env')
load_dotenv(dotenv_path)
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', default='True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    'homepage.apps.HomepageConfig',
    'users.apps.UsersConfig',
    'core.apps.CoreConfig',
    'chat',
    'channels',
    'grappelli',
    'tinymce',
    'sorl.thumbnail',

    'imagekit',
    'ckeditor',
    'ckeditor_uploader',
    'colorful',
    'adminsortable',
    'djeym',

    'django_cleanup.apps.CleanupConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'gotohome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
ASGI_APPLICATION = "gotohome.asgi.application"
WSGI_APPLICATION = 'gotohome.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev'
]
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Duck123321@yandex.ru'
EMAIL_HOST_PASSWORD = 'Remygaga123321'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_URL = 'auth/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'users.CustomUser'

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_FILENAME_GENERATOR = 'djeym.utils.get_filename'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False  # False - Only image files. (At your discretion)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
    },
    'djeym': {
        'toolbar': 'full',
        'height': 400,
        'width': 362,
        'colorButton_colors': 'F44336,C62828,E91E63,AD1457,9C27B0,6A1B9A,'
                              '673AB7,4527A0,3F51B5,283593,2196F3,1565C0,'
                              '03A9F4,0277BD,00BCD4,00838F,009688,00695C,'
                              '4CAF50,2E7D32,8BC34A,558B2F,CDDC39,9E9D24,'
                              'FFEB3B,F9A825,FFC107,FF8F00,FF9800,EF6C00,'
                              'FF5722,D84315,795548,4E342E,607D8B,37474F,'
                              '9E9E9E,424242,000000,FFFFFF',
        'colorButton_enableAutomatic': False,
        'colorButton_enableMore': True
    }
}

CSRF_COOKIE_HTTPONLY = False

DJEYM_YMAPS_API_KEY = 'dce4abe7-656d-4250-9aa9-15ea26717341'
DJEYM_YMAPS_API_KEY_FOR_ENTERPRISE = False
DJEYM_YMAPS_DOWNLOAD_MODE = 'debug' if DEBUG else 'release'


if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    INSTALLED_APPS += [
        'debug_toolbar',
    ]
    INTERNAL_IPS = ['127.0.0.1', ]

    import mimetypes
    mimetypes.add_type("application/javascript", ".js")

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
