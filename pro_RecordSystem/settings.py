"""
Django settings for pro_RecordSystem project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8zwy!9kf@(e+pf5fn*7kj*7lv=d4n(*v%4%%)d)jtn3-yu$+=2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '192.168.1.165']


# Application definition
INSTALLED_APPS = [
    #注册本项目的应用程序
    'app_HomePage.apps.AppHomepageConfig',
    'app_RecordTime.apps.AppRecordtimeConfig',
    'app_RecordMoney.apps.AppRecordmoneyConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'pro_RecordSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'pro_RecordSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        #SQLite服务器设置
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        

        #MySQL服务器设置
        #'ENGINE': 'django.db.backends.mysql',      # 数据库引擎
        #'NAME': 'record_system',                   # 数据库名称
        #'USER': 'root',                            # 链接数据库的用户名
        #'PASSWORD': '',                            # 链接数据库的密码，配置为空表示无密码
        #'HOST': '',                                # mysql服务器的域名和ip地址，配置为空表示连接的的是当前的PC
        #'PORT': '3306',                            # mysql的一个端口号,默认是3306
        

        #PostgreSQL服务器设置
        'ENGINE': 'django.db.backends.postgresql',      # 数据库引擎
        'NAME': 'record-system',                        # 数据库名称
        'USER': 'postgres',                             # 链接数据库的用户名
        'PASSWORD': '330715',                           # 链接数据库的密码，配置为空表示无密码
        'HOST': '',                                     # 服务器的域名和ip地址，配置为空表示连接的的是当前的PC
        'PORT': '5432'                                  # 端口号,默认是5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

#将UTC时间改为上海时间
#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), # 这里的"static"字符串参数为静态文件夹相对于工程根目录的相对位置
)

STATIC_URL = '/static/'


'''
本项目的单独设置
'''

# 部署至Heroku的设置
if os.getcwd() == '/app':
    import dj_database_url

    DATABASES = {
                 'default': dj_database_url.config(default='postgres://localhost')
                }

    # 让request.is_secure()承认X-Forwarded-Proto头
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # 支持所有的主机头（host header）
    ALLOWED_HOSTS = ['*']

    # 静态资产配置
    BASE_DIR         = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT      = 'staticfiles'
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )
