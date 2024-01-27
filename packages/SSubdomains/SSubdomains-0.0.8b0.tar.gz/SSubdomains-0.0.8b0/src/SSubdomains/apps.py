from django.apps import AppConfig


class SSubdomainsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SSubdomains'
#     load config for SSubdomains from .config.py
    def ready(self):
        import SSubdomains.config

#     set config for SSubdomains


