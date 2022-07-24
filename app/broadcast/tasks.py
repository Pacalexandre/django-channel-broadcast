""" Entradas do Celery de tarefas que vão trabalhar jundo com os brokers"""

import requests
from random import randint
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task

channel_layer = get_channel_layer()

@shared_task
def get_joke():
    """ Tarefa de recuperar a piada"""
    url = 'http://api.icndb.com/jokes/ramdom'
    response = requests.get(url).json()
    index = randint(1,574)
    joke = response['value'][index]['joke']

    async_to_sync(channel_layer.group_send)('jokes',{'type':'send_jokes','text': joke})
