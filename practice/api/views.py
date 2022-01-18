from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def firstView(request):
    return JsonResponse("this is the first view", safe=False)


@api_view(['GET'])
def responseTest(request):
    return Response('test response')


@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    # return Response(serializer.data)
    return JsonResponse(serializer.data, safe=False)
