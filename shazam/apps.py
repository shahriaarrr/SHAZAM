from django.apps import AppConfig


class ShazamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shazam'

    def ready(self):
        import shazam.signals
