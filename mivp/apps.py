from django.apps import AppConfig


class MivpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mivp'
    def ready(self):
        import mivp.signals




   
