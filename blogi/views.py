from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def postaukset(request):
    return render(request, 'blogi/postauslista.html')
    