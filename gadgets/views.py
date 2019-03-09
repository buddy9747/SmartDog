from django.shortcuts import render
from .models import Catlog,Product
# Create your views here.
def home(request):
    a=Catlog.objects.all()
    s=set([i.title for i in a])
    d={}
    for i in s:
        x = Catlog.objects.filter(title=i)
        sub = [j.category for j in x]
        d[i] = sub

    return render(request,"gadgets/home.html",{"menus":d})

def summary(request,menu):
    a=Catlog.objects.get(category=menu)
    return render(request,"gadgets/summary.html",{"cat":a})

def cart(request):
    return render(request,"gadgets/cart.html")


def expert(request):
    return render(request,"gadgets/experts.html")

def dogtrain(request):
    return render(request,"gadgets/dog_training.html")

def dogwash(request):
    return render(request,"gadgets/dog_selfwash.html")

def doggroom(request):
    return render(request,"gadgets/dog_grooming.html")

def dogsit(request):
    return render(request,"gadgets/dog_sitting.html")

def petadopt(request):
    return render(request,"gadgets/pet_adoptions.html")

def vetercare(request):
    return render(request,"gadgets/veterinary_care.html")