
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from todo.models import Todo
from django.contrib.auth.decorators import login_required

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == "GET":
        todos = Todo.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, "todo/index.html", context)
    else:
        return HttpResponse('Invalid request method', status=405)


@login_required(login_url='/user/login/')
@csrf_exempt
def create(request):
    if request.method == "POST":
        Todo.objects.create(
            content=request.POST['content'],
            user=request.user,
            image=request.FILES.get("image"),
        )
        return redirect('/todo/')
    elif request.method == "GET":
        return render(request, "todo/create.html")
    else:
        return HttpResponse('Invalid request method', status=405)


def read(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, "todo/read.html", context)


@csrf_exempt
def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.content = request.POST['content']
            todo.save()
            return redirect(f'/todo/{todo_id}/')
        else:
            return HttpResponse('not allowed to update', status=403)
    elif request.method == "GET":
        todo = Todo.objects.get(id=todo_id)
        context = {
            'todo': todo,
        }
        return render(request, "todo/update.html", context)
    else:
        return HttpResponse('Invalid request method', status=405)


@csrf_exempt
def delete(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return redirect('/todo/individual/')
        else:
            return HttpResponse('not allowed to delete', status=403)
    else:
        return HttpResponse('Invalid request method', status=405)


@csrf_exempt
def is_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        Todo.is_completed = True
        todo.save()
        return redirect('/todo/')
    else:
        return HttpResponse('Invalid request method', status=405)


@csrf_exempt
def individual(request):
    print(request.method)
    if request.method == "POST":
        todos = Todo.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, "todo/individual.html", context)
    elif request.method == "GET":
        todos = Todo.objects.all()
        context = {
            'todos': todos,
        }
        return render(request, "todo/individual.html", context)
    else:
        return HttpResponse('Invalid request method', status=405)
