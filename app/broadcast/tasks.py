""" Entradas do Celery de tarefas que vão trabalhar jundo com os brokers"""
import requests
from celery import shared_task

@shared_task
def get_joke():
    """ Tarefa de recuperar a piada"""
    url = 'http://api.icndb.com/jokes/ramdom'
    response = requests.get(url).json()
    joke = response.get('value')[0]

    print(joke)
    return joke
