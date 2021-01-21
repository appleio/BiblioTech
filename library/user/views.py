from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from .models import Book

class NewFormBook(forms.Form):
    title=forms.CharField(label="Title ")
    author=forms.CharField(label="Author")

# Create your views here.
def index(request):
    return render(request, "user/index.html")

def login(request):
    return render(request, "user/index.html")

def logout(request):
    pass

def books(request):
    if request.method == 'POST':
        form=NewFormBook(request.POST)
        if form.is_valid():
            Book.objects.create(title=form.cleaned_data["title"],author=form.cleaned_data["author"])
            return HttpResponseRedirect("/user/books")
    return render(request, "user/books.html",{
        "books":Book.objects.all(),
        "form":NewFormBook()
    })