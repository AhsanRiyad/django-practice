from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def firstView(request):
    return JsonResponse("this is the first view", safe=False)
