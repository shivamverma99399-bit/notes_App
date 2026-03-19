from urllib import request

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note

def home(request):
    if request.method == "POST":
        note = request.POST.get('note')
        #print(note)   # terminal me dikhega
        Note.objects.create(text=note)
    notes = Note.objects.all()   # 🔥 ye line important
    
    return render(request, 'home.html', {'notes': notes})
def delete_note(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/')