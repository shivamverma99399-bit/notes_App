from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('/login/')
    return render(request, 'signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')


def home(request):
    if request.method == "POST":
        note_text = request.POST.get('note')
        if note_text:
            Note.objects.create(text=note_text)
        return redirect('/')   # 🔥 important

    notes = Note.objects.all().order_by('-id')
    return render(request, 'home.html', {'notes': notes})
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/')
def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == "POST":
        new_text = request.POST.get('note')
        note.text = new_text
        note.save()
        return redirect('/')

    return render(request, 'edit.html', {'note': note})