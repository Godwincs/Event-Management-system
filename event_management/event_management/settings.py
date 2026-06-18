from pathlib import Path
import os

# =====================================
# BASE DIRECTORY
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================
# SECURITY
# =====================================

SECRET_KEY = 'django-insecure-change-this-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

# =====================================
# APPLICATIONS
# =====================================

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'events',
]

# =====================================
# MIDDLEWARE
# =====================================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =====================================
# ROOT URL
# =====================================

ROOT_URLCONF = 'event_management.urls'

# =====================================
# TEMPLATES
# =====================================

TEMPLATES = [
    {
        'BACKEND':
        'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            os.path.join(
                BASE_DIR,
                'templates'
            )
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

# =====================================
# WSGI
# =====================================

WSGI_APPLICATION = 'event_management.wsgi.application'

# =====================================
# DATABASE (SQLite)
# =====================================

DATABASES = {

    'default': {

        'ENGINE':
        'django.db.backends.sqlite3',

        'NAME':
        BASE_DIR / 'db.sqlite3',
    }
}

# =====================================
# PASSWORD VALIDATION
# =====================================

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# =====================================
# INTERNATIONALIZATION
# =====================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True

# =====================================
# STATIC FILES
# =====================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(
        BASE_DIR,
        'static'
    )
]

STATIC_ROOT = os.path.join(
    BASE_DIR,
    'staticfiles'
)

# =====================================
# MEDIA FILES
# =====================================

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(
    BASE_DIR,
    'media'
)

# =====================================
# DEFAULT PRIMARY KEY
# =====================================

DEFAULT_AUTO_FIELD = (
    'django.db.models.BigAutoField'
)

# =====================================
# LOGIN / LOGOUT
# =====================================

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

# =====================================
# EMAIL CONFIGURATION
# =====================================

EMAIL_BACKEND = (
    'django.core.mail.backends.smtp.EmailBackend'
)

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'godwincs2003@gmail.com'

EMAIL_HOST_PASSWORD = 'GODWINCS2003'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# =====================================
# SECURITY SETTINGS
# =====================================

CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SECURE = False

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True