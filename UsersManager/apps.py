from django.apps import AppConfig


class UsersmanagerConfig(AppConfig):
    name = 'UsersManager'

    def ready(self):
        import UsersManager.signals
