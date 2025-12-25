from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('test view & URL routing working!')

def home(request):
    return render(request, 'home.html')