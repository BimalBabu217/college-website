from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, "website/index.html")

def home_view(request):
  return render(request, "website/home.html")