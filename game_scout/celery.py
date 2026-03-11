import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game_scout.settings.dev")

app = Celery("game_scout")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
