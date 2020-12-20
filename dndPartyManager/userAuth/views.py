from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from django.contrib.auth import authenticate, login

@api_view(['GET'])
def currentUser(request):
    user = request.user
    return Response({
        'username': user.username,
        'id': user.id,
    })