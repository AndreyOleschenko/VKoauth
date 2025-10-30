"""
Django settings for VKoauth project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-pl+#w(_1x@uevc1c6kk8v279z*2_n9+ul&l_a#w)wy7e-+bkh!'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.loca.lt', 'brave-coins-wink.loca.lt']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000', 'https://brave-coins-wink.loca.lt']

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'users',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.yandex',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'VKoauth.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'VKoauth.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.loca.lt',
    'brave-coins-wink.loca.lt',
    '0.0.0.0'  # Добавляем 0.0.0.0
]

SITE_ID = 1
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# allauth settings - определяются непосредственно
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_LOGIN_METHODS = ['email']
ACCOUNT_EMAIL_VERIFICATION = 'none'#Раскомментировал, чтобы избежать проблем с настройкой email-backend
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_FIELDS = ['email'] #Упростил поля регистрации


# allauth settings - в случае если VK APP использует ссылку с 127.0.0.1
# то нужно указать redirect_uri с 127.0.0.1, иначе localhost

# VK OAuth settings
SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        'APPS': [{
            'client_id': '54119959',
            'secret': 'W6WPjAdWRjNOpgF3eRIT',
            'key': '',
        }],
    },

    'yandex': {
        'APPS': [{
            'client_id': '4b4e18a8c7fc4cd6be2704cc4751855f',
            'secret': '033e03cd5c9f4904907bb95c5822f276',
            'key': '',
        }],
        'SCOPE': ['login:email', 'login:info'],
        'AUTH_PARAMS': {
            'code_challenge_method': 'S256'
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
