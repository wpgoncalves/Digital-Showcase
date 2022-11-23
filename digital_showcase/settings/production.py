from cloudinary import config as cloudinary_config

from digital_showcase.settings.common import BASE_DIR, Path, env

# Load environment variable values
env.read_env(Path.joinpath(BASE_DIR.parent, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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
    'rest_framework',
    'cloudinary',
    'global_models',
    'newsletter',
    'customers',
    'products',
    'showcase',
    'stores',
    'about',
    'cart',
    'api',
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

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASSWORD'),
        'HOST': env.str('DATABASE_HOST'),
        'PORT': env.str('DATABASE_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# Cloudinary settings
# https://github.com/klis87/django-cloudinary-storage#readme

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env.str('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': env.str('CLOUDINARY_API_KEY'),
    'API_SECRET': env.str('CLOUDINARY_API_SECRET'),
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
