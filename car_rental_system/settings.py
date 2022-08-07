#IMPORTS
import os

#BASE DIRECTORY
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#SECRET KEY
SECRET_KEY = '^imyfuo7z!%$s=(jhzvzz#4o3y@p29aeqk3$+9tjmvwfet@+zq'

#DEBUG - TRUE IN PRODUCTION - FALSE IN DEPLOYMENT
DEBUG = True

#ALLOWED HOSTS
ALLOWED_HOSTS = ['broncorentals.herokuapp.com', '0.0.0.0','192.168.1.160', '127.0.0.1', '76.203.142.218', 'a6ecef2437ee.ngrok.io']


#INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reservations.apps.ReservationsConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'car_rental_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/build')
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

WSGI_APPLICATION = 'car_rental_system.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#META INFORMATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

DATETIME_FORMAT="Y-m-d H:i"

USE_I18N = True

USE_L10N = False

USE_TZ = False

#STATIC FILES
#MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/build/static')
]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'

#LOGIN
LOGIN_REDIRECT_URL = 'main-home'
LOGIN_URL = 'login'

#EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'broncoscarrentalsystem@gmail.com'
EMAIL_HOST_PASSWORD = 'CarRentalPassword'
