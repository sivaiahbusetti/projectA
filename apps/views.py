from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def siva(request):
    return HttpResponse('<h1>hello siva</h1>')

def kumar(request):
    return HttpResponse('<h1>hello kumar</h1>')