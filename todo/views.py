
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo

# Create your views here.


def index(requset):
    return render(requset, "todo/index.html")


@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(content=request.POST['content'])
        return redirect('/todo/')
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse('error', status=405)
