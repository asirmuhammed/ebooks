from django.shortcuts import render
from .models import Book

# Create your views here.
def Index (request):
    context={
        'books':Book.objects.all()
    }
    return render (request,'web/index.html',context)

def Signup (request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email', '')
        password = request.POST['password']
        # Perform validation and database operations here
        # For simplicity, let's assume the data is stored successfully
        return render(request, 'web/login.html', {'username': username})
    else:
        
        return render (request,'web/signup.html',context)

def Login (request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Perform validation and authentication here
        # For simplicity, let's assume the login is successful
        return render(request, 'web/index.html', {'username': username})
    else:
        return render(request, 'web/login.html')

def books_detail (request):
    context={}
    return render (request,'web/books-detail.html',context)

# def About (request):
#     context={}
#     return render (request,'web/index.html',context)
