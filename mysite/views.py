from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'mainpage.html', {})

def inventory(request):
    return render(request, 'inventorypage.html', {})

def pantries(request):
    return render(request, 'findpantrypage.html', {})

def add(request):
    return render(request, 'additemspage.html', {})

def remove(request):
    return render(request, 'removeitemspage.html', {})

def index(request):
    return render(request, 'index.html', {})

##def login(request):
  #  return render(request, 'register/login.html', {})
