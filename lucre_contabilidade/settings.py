from pathlib import Path
import os
import dj_database_url
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'collected-media'

S3_ENABLED = config('S3_ENABLED', cast=bool, default=False)
LOCAL_SERVE_MEDIA_FILES = config('LOCAL_SERVE_MEDIA_FILES', cast=bool, default=not S3_ENABLED)

if S3_ENABLED:
    AWS_ACCESS_KEY_ID = config('BUCKETEER_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('BUCKETEER_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('BUCKETEER_BUCKET_NAME')
    AWS_S3_REGION_NAME = config('BUCKETEER_AWS_REGION')
    AWS_DEFAULT_ACL = None
    AWS_S3_SIGNATURE_VERSION = config('S3_SIGNATURE_VERSION', default='s3v4')
    AWS_S3_ENDPOINT_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

if not LOCAL_SERVE_MEDIA_FILES:
    PUBLIC_MEDIA_LOCATION = 'media/public'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'lucre_contabilidade.utils.storage_backends.PublicMediaStorage'

    PRIVATE_MEDIA_LOCATION = 'media/private'
    PRIVATE_FILE_STORAGE = 'lucre_contabilidade.utils.storage_backends.PrivateMediaStorage'


if not LOCAL_SERVE_MEDIA_FILES and not S3_ENABLED:
    raise ValueError('S3_ENABLED must be true if media files are not served locally')


DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,  # Mantém a conexão aberta por mais tempo
        ssl_require=True   # Exige conexão SSL para maior segurança no Heroku
    )
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'lucre_db',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432', 
#         'OPTIONS': {
#             'sslmode': 'disable',
#         },
#     }
# }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-71p+jg-ul42bsk#zbncjodxn@+4oguw%0wfs_@4f+)*n1iieel'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 


# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'noticias',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'corsheaders',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ROOT_URLCONF = 'lucre_contabilidade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'lucre_contabilidade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DEFAULT_CHARSET = 'utf-8'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

AWS_ACCESS_KEY_ID = config('BUCKETEER_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('BUCKETEER_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('BUCKETEER_BUCKET_NAME')
AWS_S3_REGION_NAME = config('BUCKETEER_AWS_REGION')
AWS_DEFAULT_ACL = None
AWS_S3_SIGNATURE_VERSION = config('S3_SIGNATURE_VERSION', default='s3v4')
AWS_S3_ENDPOINT_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
