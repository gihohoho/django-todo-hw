from django.http import HttpResponse
from django.shortcuts import redirect, render

from user.models import User


# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect('/todo/')
    elif request.method == "GET":
        return render(request, "User/signup.html")
    else:
        return HttpResponse('Invalid request method', status=405)
