""" instanciando celery para rodar junto com o django """
from .celery import app as celery_app


__all__ = ['celery_app']