from django.shortcuts import redirect, render

# save data into the model
from todo.models import Todo

# Create your views here.
def index(request):
    # get todo object(data)
    todos = Todo.objects.all()
    # check  for POST or GET request
    # get the POST data from the html page
    if(request.method == "POST"):
        new_todo = Todo(
            title=request.POST['title']
        )
        # save to database
        new_todo.save()
        # return to the home page
        return redirect('/')
    #display the home page which is index.html and pass data along with it
    return render(request, 'index.html', {'todos': todos})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("/")