from digital_showcase.settings.common import (AUTH_PASSWORD_VALIDATORS,
                                              BASE_DIR, DEFAULT_AUTO_FIELD,
                                              GROUP_STORES_IMAGES,
                                              LANGUAGE_CODE, MEDIA_ROOT,
                                              MEDIA_URL, MESSAGE_TAGS,
                                              PWA_APP_BACKGROUND_COLOR,
                                              PWA_APP_DEBUG_MODE,
                                              PWA_APP_DESCRIPTION, PWA_APP_DIR,
                                              PWA_APP_DISPLAY, PWA_APP_ICONS,
                                              PWA_APP_ICONS_APPLE,
                                              PWA_APP_LANG, PWA_APP_NAME,
                                              PWA_APP_ORIENTATION,
                                              PWA_APP_SCOPE, PWA_APP_START_URL,
                                              PWA_APP_STATUS_BAR_COLOR,
                                              PWA_APP_THEME_COLOR,
                                              PWA_SERVICE_WORKER_PATH,
                                              ROOT_URLCONF, STATIC_ROOT,
                                              STATIC_URL, STATICFILES_DIRS,
                                              TEMPLATES, TIME_ZONE, USE_I18N,
                                              USE_TZ, WSGI_APPLICATION, env)

try:
    if env.bool('DEVELOPMENT_RUN_MODE', True):
        from digital_showcase.settings.development import (ALLOWED_HOSTS,
                                                           DATABASES, DEBUG,
                                                           INSTALLED_APPS,
                                                           MIDDLEWARE,
                                                           SECRET_KEY)
    else:
        from digital_showcase.settings.production import (ALLOWED_HOSTS,
                                                          CLOUDINARY_STORAGE,
                                                          DATABASES, DEBUG,
                                                          DEFAULT_FILE_STORAGE,
                                                          INSTALLED_APPS,
                                                          MIDDLEWARE,
                                                          SECRET_KEY,
                                                          STATICFILES_STORAGE)

except ImportError as exc_import:
    raise ImportError(
        'Unable to import configuration files.'
        'Check that all environment variables have been properly declared.'
    ) from exc_import

__all__ = [
    'ALLOWED_HOSTS',
    'AUTH_PASSWORD_VALIDATORS',
    'BASE_DIR',
    'CLOUDINARY_STORAGE',
    'DATABASES',
    'DEBUG',
    'DEFAULT_AUTO_FIELD',
    'DEFAULT_FILE_STORAGE',
    'env',
    'GROUP_STORES_IMAGES',
    'INSTALLED_APPS',
    'LANGUAGE_CODE',
    'MEDIA_ROOT',
    'MEDIA_URL',
    'MESSAGE_TAGS',
    'MIDDLEWARE',
    'PWA_APP_BACKGROUND_COLOR',
    'PWA_APP_DEBUG_MODE',
    'PWA_APP_DESCRIPTION',
    'PWA_APP_DIR',
    'PWA_APP_DISPLAY',
    'PWA_APP_ICONS',
    'PWA_APP_ICONS_APPLE',
    'PWA_APP_LANG',
    'PWA_APP_NAME',
    'PWA_APP_ORIENTATION',
    'PWA_APP_SCOPE',
    'PWA_APP_START_URL',
    'PWA_APP_STATUS_BAR_COLOR',
    'PWA_APP_THEME_COLOR',
    'PWA_SERVICE_WORKER_PATH',
    'ROOT_URLCONF',
    'SECRET_KEY',
    'STATICFILES_DIRS',
    'STATICFILES_STORAGE',
    'STATIC_ROOT',
    'STATIC_URL',
    'TEMPLATES',
    'TIME_ZONE',
    'USE_I18N',
    'USE_TZ',
    'WSGI_APPLICATION'
]
