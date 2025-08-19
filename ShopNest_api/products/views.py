from django.shortcuts import render
from django.http import JsonResponse

def product_list(request):
    return JsonResponse({"message": "List of products"})

# Create your views here.
