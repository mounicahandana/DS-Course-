from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demoresp(request):
    return HttpResponse('This Is Response')