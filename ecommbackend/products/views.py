from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(('GET',))
def products(request):
    return Response('this is product page')