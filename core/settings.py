from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 SEGURANÇA
SECRET_KEY = 'django-insecure-1*u35z$zfm$ch_*#77cm7%v5n213fm@_gkun1$8kgn*$-o^!*$'

# 🧪 DEBUG dinâmico (local vs produção)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# 🌐 HOSTS liberados
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.onrender.com']

# 📦 APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',  # 👈 ESSENCIAL
]

# ⚙️ MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

# 🧠 TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 👈 pasta templates global
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# 🗄️ DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔑 VALIDAÇÃO DE SENHA
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 INTERNACIONALIZAÇÃO
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# 📁 ARQUIVOS ESTÁTICOS
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # 👈 sua pasta local
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # 👈 produção (Render)

# 🔧 DEFAULT
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'