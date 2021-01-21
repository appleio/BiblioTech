from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.db import models
from user.models import Book
from .models import Library

libraries = []

CHOICES=[
    ("private","Private"),("public","Public")
]

class NewFormLibrary(forms.Form):
    title=forms.CharField(label="What is your library name?")
    description=forms.CharField(widget=forms.Textarea,label="Add a description of your library: ")
    privacy=forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class NewFormBook(forms.Form):
    title=forms.CharField(label="What is the name of the book?")
    author=forms.CharField(label="Author: ")

def index(request):
    return render(request, "community/index.html", {
        "list":Library.objects.all()
    })

def create(request):
    if request.method == "POST":
        form=NewFormLibrary(request.POST)
        if form.is_valid():
            Library.objects.create(title=form.cleaned_data["title"],description=form.cleaned_data["description"],privacy=form.cleaned_data["privacy"])
            return HttpResponseRedirect("/")    
    return render(request, "community/create.html",{
        "form":NewFormLibrary()
    }) 


'''
def create(request):
    if request.method == "POST":
        form=NewFormLibrary(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            privacy = form.cleaned_data['privacy']
            library = {
                'title':title,
                'description':description, 
                'privacy':privacy
            }    
            libraries.append(library)
            return HttpResponseRedirect("/")
        else:
            return render(request, "community/create.html", {
                "form":NewFormLibrary()
            })
    return render(request, "community/create.html",{
        "form":NewFormLibrary()
    })
'''

def library(request,title):
    library=Library.objects.get(title=title)
    books=library.books.all()
    return render(request, "community/library.html",{
        "data": Library.objects.all(),
        "title":title,
        "books":books
    })

def profile(request):
    return render(request, "community/profile.html")
    
