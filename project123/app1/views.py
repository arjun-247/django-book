from django.shortcuts import render

# Create your views here.
from app1.models import *
from app1.form import *


def base(request):
    return render(request,'base.html')


def upload(request):
    form=bookform()
    if(request.method=="POST"):
        form=bookform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return base(request)
    return render(request,'add_book.html',{'form':form})

def booklist(request):
    b=Book.objects.all()
    return render(request,'list.html',{'b':b})
