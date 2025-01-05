"""
Django settings for gipfel_tutor project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
import sys
import dj_database_url
from pathlib import Path
from django.core.management.utils import get_random_secret_key

if os.path.isfile("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# This will only make DEBUG = True if the environment variable is set to "True"
# DEBUG = os.environ.get("DEBUG", "") == "True"

# Separate Development variable for db, email backend and S3 bucket
# DEVELOPMENT = os.environ.get("DEVELOPMENT", "") == "False"
DEBUG = False
DEVELOPMENT = True
ALLOWED_HOSTS = [
    ".herokuapp.com",
    "localhost",
    "127.0.0.1",
    ".vercel.app",
    ".now.sh"
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
    "localflavor",
    "core",
    "tutor_market",
    "booking",
    "calendly",
    
    
]
SITE_ID = 1  # Ensure this is set
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


# -> Credit for retrieving the email address: https://github.com/pennersr/django-allauth/issues/330  # noqa
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_SESSION_REMEMBER = True

# if DEVELOPMENT:
CALENDLY_CLIENT_ID = os.environ.get("CALENDLY_DEV_CLIENT_ID", "s3Inn4DKEVBbosK79rZCBZ6XrWGd8adljopDQNpw5PA")
CALENDLY_CLIENT_SECRET = os.environ.get("CALENDLY_DEV_CLIENT_SECRET", "nZP6IerDsSbP_o2AQYKIn391D38ampzrZdYGS7Allkk")
CALENDLY_REDIRECT_URI = os.environ.get("CALENDLY_DEV_REDIRECT_URI", "http://localhost:8000/calendly/auth")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "gipfeltutor@example.com"
SITE_ID = 1
# else:
#     CALENDLY_CLIENT_ID = os.environ.get("CALENDLY_PROD_CLIENT_ID", "s3Inn4DKEVBbosK79rZCBZ6XrWGd8adljopDQNpw5PA")
#     CALENDLY_CLIENT_SECRET = os.environ.get("CALENDLY_PROD_CLIENT_SECRET", "nZP6IerDsSbP_o2AQYKIn391D38ampzrZdYGS7Allkk")
#     CALENDLY_REDIRECT_URI = os.environ.get("CALENDLY_PROD_REDIRECT_URI", "http://localhost:8000/calendly/auth")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "asadullah7370@gmail.com")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS", "suzqsiuijgmuxagv")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SITE_ID = 2

LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

ROOT_URLCONF = "gipfel_tutor.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

SOCIALACCOUNT_ENABLED = True

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

WSGI_APPLICATION = "gipfel_tutor.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if 'test' in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
elif "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
             "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'railway',
        "USER": 'postgres',
        "PASSWORD": 'nAVDwFeOoVeAlykZcXHqsYPIspuYaRpW',
        "HOST": 'autorack.proxy.rlwy.net',
        "PORT": '13540',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static and Media Files
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

if not os.environ.get("USE_AWS"):  # Local Development
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:  # Production with AWS S3
    # Cache Control for AWS
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }

    # AWS Bucket Config
    AWS_STORAGE_BUCKET_NAME = "gipfel-tutor-768a610dc54f"
    AWS_S3_REGION_NAME = "eu-north-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and Media Files for AWS
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"

    # URLs
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STRIPE_CURRENCY = "eur"
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_51QZQgKP0fgoIcLs3916GnUdTKYzrvqSgH4L8yPGmIEmN8XYikzhjxPI5zcbggwhwQYBmf0IMpj8ZaojbkegoKwHe00CuEBqIe7")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_51QZQgKP0fgoIcLs3LUXel20tDn1dj5WBD156ucaykZGpecUjCO477wIkoMjnlIJpRJ3dNApAGhQPr9xnUjWxVA7e00UgLTIi1z")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "whsec_YVowh8wZOdPNzJU0xPCrt1PQGKrg06rj")
