from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

# Create your views here.
def index(request):
  if request.user.is_authenticated:
    return render(request, 'users/index.html')
  else:
    return render(request, 'users/login.html')
    # return HttpResponseRedirect(reverse("login"))
  
def login_view(request):
  if request.method == "POST":
    username = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=username , password=password)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("index"))
    else:
      return render(request, "users/login.html", {
				"message": "Invalid username or password"
			})
    
  return render(request, "users/login.html") 

def logout_view(request):
  pass