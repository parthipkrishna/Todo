from django.shortcuts import render,redirect, HttpResponse
from . forms import TodoForm
from . models import Todo

# Create your views here.
def home(request):
    form=TodoForm()
    ttoddo=Todo.objects.all()
    context = {
        'forms': form,
        'ttoddo': ttoddo,
    }
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request,'index.html',context)

def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=='POST':
    
        todo.delete()
        return redirect("home")

def update(request,id):
    todo=Todo.objects.get(id=id)
    form=TodoForm(instance=todo)
    context={
        'form':form,
        
    }
    if request.method=='POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
        
            form.save()
            return redirect('home')
    return render(request,'update.html',context)
    

    
