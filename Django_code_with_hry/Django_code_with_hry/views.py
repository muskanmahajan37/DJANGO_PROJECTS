from django.http import HttpResponse
import os

def index(request):
    return HttpResponse('''
    <h1>hello<h1>
    ''')