from django.apps import AppConfig
import asyncio
import logging


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .coroutine import sub_test
        sub_test(repeat=10)

        