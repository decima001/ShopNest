from django.shortcuts import render
from django.http import JsonResponse

def user_list(request):
    return JsonResponse({"message": "List of users"})

# Create your views here.
