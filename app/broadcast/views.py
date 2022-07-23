""" View File """
from django.shortcuts import render


def index(request):
    """ view raiz do sistema """
    return render(request, 'index.html')
