from django.shortcuts import render,redirect
from .models import Student
from .forms import StudForm

def index(request):
    sdetails=Student.objects.all()
    return render(request,'fbv/index.html',{'s':sdetails})


def add(request):
    form=StudForm()
    if request.method=='POST':
        form=StudForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'fbv/add.html', {'form':form})


def dele(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('/')

def upd(request,id):
    s=Student.objects.get(id=id)
    form=StudForm(instance=s)
    if request.method=='POST':
        form=StudForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'fbv/update.html',{'form':form})



# Create your views here.
