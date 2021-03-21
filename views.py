from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    # create a variable todo_items to store all items in the database
    todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
#create a dictionary
                  {"all_items": todo_items})

def addTodo(request):
    new_item = TodoItem(content=request.POST["content"])
    new_item.save()
    return HttpResponseRedirect('/TODO/')

def deleteTodo(request,todo_id):
    item_delete = TodoItem.objects.get(id=todo_id)
    item_delete.delete()
    return HttpResponseRedirect('/TODO/')

