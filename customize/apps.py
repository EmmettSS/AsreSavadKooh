from django.apps import AppConfig


class CustomizeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customize'
    verbose_name = "مدیریت سایت"