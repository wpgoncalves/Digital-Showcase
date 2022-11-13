from pathlib import Path

from cloudinary import config as cloudinary_config
from django.contrib.messages import constants as messages
from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Create an instance of django-environ and load environment variable values.
# The .env file is not versioned.
env = Env()
env.read_env(Path.joinpath(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DJANGO_DEBUG', bool, False)

if DEBUG:
    ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']
else:
    ALLOWED_HOSTS = ['digitalshowcase.pythonanywhere.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'cloudinary',
    'global_models',
    'newsletter',
    'customers',
    'products',
    'showcase',
    'stores',
    'about',
    'cart',
    'app',
    'pwa',
    'django_cleanup.apps.CleanupConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digital_showcase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'digital_showcase.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if DEBUG:
    DB_PARAMETERS = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
else:
    DB_PARAMETERS = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
        'OPTION': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }

DATABASES = {
    'default': DB_PARAMETERS
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa: E501
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa: E501
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = Path.joinpath(BASE_DIR, 'static')

STATICFILES_DIRS = [
    ('css', Path.joinpath(STATIC_ROOT, 'css')),
    ('favicons', Path.joinpath(STATIC_ROOT, 'favicons')),
    ('img', Path.joinpath(STATIC_ROOT, 'img')),
    ('js', Path.joinpath(STATIC_ROOT, 'js'))
]

MEDIA_URL = 'media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')

# Cloudinary settings
# https://github.com/klis87/django-cloudinary-storage#readme

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env('CLOUDINARY_API_KEY'),
    'API_SECRET': env('CLOUDINARY_API_SECRET'),
    'SECURE': True,
    'MEDIA_TAG': 'digital_showcase_media',
    'INVALID_VIDEO_ERROR_MESSAGE': 'Carregue um arquivo de vídeo válido.',
    'EXCLUDE_DELETE_ORPHANED_MEDIA_PATHS': (),
    'STATIC_TAG': 'digital_showcase_static',
    'STATICFILES_MANIFEST_ROOT': Path.joinpath(BASE_DIR, 'manifest'),
    'STATIC_IMAGES_EXTENSIONS': ['jpg', 'jpe', 'jpeg', 'jpc', 'jp2', 'j2k',
                                 'wdp', 'jxr', 'hdp', 'png', 'gif', 'webp',
                                 'bmp', 'tif', 'tiff', 'ico'],
    'STATIC_VIDEOS_EXTENSIONS': ['mp4', 'webm', 'flv', 'mov', 'ogv', '3gp',
                                 '3g2', 'wmv', 'mpeg', 'flv', 'mkv', 'avi']
}

cloudinary_config(api_proxy='http://proxy.server:3128')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  # noqa: E501

# Service worker and Manifest.json file data(PWABuilder)
# https://github.com/silviolleite/django-pwa

PWA_SERVICE_WORKER_PATH = Path.joinpath(STATIC_ROOT, 'js', 'pwabuilder-sw.js')
PWA_APP_DEBUG_MODE = False

PWA_APP_BACKGROUND_COLOR = '#f5f5f5'
PWA_APP_DESCRIPTION = 'Vitrine Digital, as melhores oportunidades e ofertas da sua região na sua vitrine pessoal.'  # noqa: E501
PWA_APP_DIR = 'ltr'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_NAME = 'Vitrine Digital'
PWA_APP_ORIENTATION = 'any'
PWA_APP_SCOPE = '/'
PWA_APP_START_URL = '/'
PWA_APP_THEME_COLOR = '#2180A7'
PWA_APP_ICONS = [
    {
        "src": "/static/favicons/favicon-32x32.png",
        "type": "image/png",
        "sizes": "32x32"
    },
    {
        "src": "/static/favicons/favicon-16x16.png",
        "type": "image/png",
        "sizes": "16x16"
    },
    {
        "src": "/static/favicons/favicon.ico",
        "type": "image/x-icon"
    },
    {
        "src": "/static/favicons/android-chrome-192x192.png",
        "type": "image/png",
        "sizes": "192x192"
    },
    {
        "src": "/static/favicons/android-chrome-512x512.png",
        "type": "image/png",
        "sizes": "512x512"
    }
]
PWA_APP_ICONS_APPLE = [
    {
        "src": "/static/favicons/apple-touch-icon.png",
        "type": "image/png",
        "sizes": "180x180"
    },
]
PWA_APP_LANG = 'pt-BR'
PWA_APP_STATUS_BAR_COLOR = 'default'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Defines message type constants
# https://docs.djangoproject.com/en/4.0/ref/settings/#messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-primary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Defines the description and image that represent the store groups.

GROUP_STORES_IMAGES = {
    'Doceria': ('stores/img/group-candy.jpg', 'cake'),
    'Lanchonete': ('stores/img/group-snack-bars.jpg', 'coffee'),
    'Pizzaria': ('stores/img/group-pizzerias.jpg', 'local_pizza'),
    'Restaurante': ('stores/img/group-restaurants.jpg', 'restaurant'),
    'Vestuário': ('stores/img/group-clothing.jpg', 'checkroom'),
    'Cosméticos': ('stores/img/group-cosmetics.jpg', 'brush')
}
