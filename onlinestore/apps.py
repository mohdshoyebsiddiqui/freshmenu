from django.apps import AppConfig


class OnlinestoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onlinestore'

    def ready(self):
        import onlinestore.signals
