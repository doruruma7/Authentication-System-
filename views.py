from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout


# Create your views here.
def index(request):
  if request.user.is_anonymous:
    return redirect("/login")
  return render(request, 'index.html')


def loginuser(request):
  if request.method == "post":
    username = request.post.get('username'),
    password = request.post.get('password')
    user = authenticate(username='username', password='password')
    if user is not None:
      login(user)
      redirect('/')
    else:
      return render(request, 'login.html')


def logoutuser(request):
  logout(request)
  return redirect('/login')
