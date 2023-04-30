from pathlib import Path
from idempotency_key import status

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-8ly@&l3!na4e1ukj5^cza-#ud&9#&$6mu#6_vr9#min0fyl2x4"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "idempotency_key.middleware.IdempotencyKeyMiddleware",
]

MIGRATION_MODULES = {"app": "app.infrastructure.db.migrations"}

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     "DEFAULT_PERMISSION_CLASSES": [
#         "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
#     ]
# }

IDEMPOTENCY_KEY = {
    # Specify the key encoder class to be used for idempotency keys.
    # If not specified then defaults to 'idempotency_key.encoders.BasicKeyEncoder'
    "ENCODER_CLASS": "idempotency_key.encoders.BasicKeyEncoder",
    # Set the response code on a conflict.
    # If not specified this defaults to HTTP_409_CONFLICT
    # If set to None then the original request's status code is used.
    "CONFLICT_STATUS_CODE": status.HTTP_409_CONFLICT,
    # Allows the idempotency key header sent from the client to be changed
    "HEADER": "HTTP_IDEMPOTENCY_KEY",
    "STORAGE": {
        # Specify the storage class to be used for idempotency keys
        # If not specified then defaults to 'idempotency_key.storage.MemoryKeyStorage'
        "CLASS": "idempotency_key.storage.MemoryKeyStorage",
        # Name of the django cache configuration to use for the CacheStorageKey storage
        # class.
        # This can be overriden using the @idempotency_key(cache_name='MyCacheName')
        # view/viewset function decorator.
        "CACHE_NAME": "default",
        # When the response is to be stored you have the option of deciding when this
        # happens based on the responses status code. If the response status code
        # matches one of the statuses below then it will be stored.
        # The statuses below are the defaults used if this setting is not specified.
        "STORE_ON_STATUSES": [
            status.HTTP_200_OK,
            status.HTTP_201_CREATED,
            status.HTTP_202_ACCEPTED,
            status.HTTP_203_NON_AUTHORITATIVE_INFORMATION,
            status.HTTP_204_NO_CONTENT,
            status.HTTP_205_RESET_CONTENT,
            status.HTTP_206_PARTIAL_CONTENT,
            status.HTTP_207_MULTI_STATUS,
        ],
    },
    # The following settings deal with the process/thread lock that can be placed around the cache storage object
    # to ensure that multiple threads do not try to call the same view/viewset method at the same time.
    "LOCK": {
        # Specify the key object locking class to be used for locking access to the cache storage object.
        # If not specified then defaults to 'idempotency_key.locks.basic.ThreadLock'
        "CLASS": "idempotency_key.locks.basic.ThreadLock",
        # Location of the Redis server if MultiProcessRedisLock is used otherwise this is ignored.
        # The host name can be specified or both the host name and the port separated by a colon ':'
        "LOCATION": "localhost:6379",
        # The unique name to be used accross processes for the lock. Only used by the MultiProcessRedisLock class
        "NAME": "MyLock",
        # The maximum time to live for the lock. If a lock is given and is never released this timeout forces the release
        # The lock time is in seconds and the default is None which means lock until it is manually released
        "TTL": None,
        # The use of a lock around the storage object so that only one thread at a time can access it.
        # By default this is set to true. WARNING: setting this to false may allow duplicate calls to occur if the timing
        # is right.
        "ENABLE": True,
        # If the ENABLE_LOCK setting is True above then this represents the timeout (in seconds as a floating point number)
        # to occur before the thread gives up waiting. If a timeout occurs the middleware will return a HTTP_423_LOCKED
        # response.
        "TIMEOUT": 0.1,
    },
}
