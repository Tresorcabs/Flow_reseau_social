from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    # ici, on importe les signaux lorsque l'application est prête
    def ready(self):
        import core.signals