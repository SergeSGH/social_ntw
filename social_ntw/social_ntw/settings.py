import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'hhz7l-ltdismtf@bzyz+rple7*s*w$jak%whj@(@u0eok^f9k4'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'djoser',
    'api.apps.ApiConfig',
    'posts.apps.PostsConfig',
    'drf_yasg'
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

ROOT_URLCONF = 'social_ntw.urls'

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

WSGI_APPLICATION = 'social_ntw.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

}

#DJOSER = {
#    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
#    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
#    'ACTIVATION_URL': '#/activate/{uid}/{token}',
#    'SEND_ACTIVATION_EMAIL': False,
#    'SERIALIZERS': {
#        'activation': 'djoser.serializers.ActivationSerializer',
#        'password_reset': 'djoser.serializers.SendEmailResetSerializer',
#        'password_reset_confirm': 'djoser.serializers.PasswordResetConfirmSerializer',
#        'password_reset_confirm_retype': 'djoser.serializers.PasswordResetConfirmRetypeSerializer',
#        'set_password': 'djoser.serializers.SetPasswordSerializer',
#        'set_password_retype': 'djoser.serializers.SetPasswordRetypeSerializer',
#        'set_username': 'djoser.serializers.SetUsernameSerializer',
#        'set_username_retype': 'djoser.serializers.SetUsernameRetypeSerializer',
#        'username_reset': 'djoser.serializers.SendEmailResetSerializer',
#        'username_reset_confirm': 'djoser.serializers.UsernameResetConfirmSerializer',
#        'username_reset_confirm_retype': 'djoser.serializers.UsernameResetConfirmRetypeSerializer',
#        'user_create': 'djoser.serializers.UserCreateSerializer',
#        'user_create_password_retype': 'djoser.serializers.UserCreatePasswordRetypeSerializer',
#        'user_delete': 'djoser.serializers.UserDeleteSerializer',
#        'user': 'api.serializers.UserSerializer',
#        'current_user': 'djoser.serializers.UserSerializer',
#        'token': 'djoser.serializers.TokenSerializer',
#        'token_create': 'djoser.serializers.TokenCreateSerializer',
#}
#}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
}
