SECRET_KEY = "not-a-secret"

INSTALLED_APPS = [
    "wagtail_charts",
    "wagtail_color_panel",
    "wagtail.admin",
    "wagtail",
    "wagtail.users",
    "wagtail.images",
    "wagtail.documents",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

STATIC_URL = "/static/"
ROOT_URLCONF = "tests.urls"
USE_TZ = True
WAGTAIL_SITE_NAME = "wagtail-charts tests"
WAGTAILADMIN_BASE_URL = "http://localhost"
