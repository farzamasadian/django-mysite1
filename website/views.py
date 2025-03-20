from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def json_test(request):
    return JsonResponse({'name':'farzam'})
