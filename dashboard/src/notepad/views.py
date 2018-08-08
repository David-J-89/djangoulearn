from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteModelForm

# Create your views here.
#CRUD
# create, update, retrieve, delete


def create_view(request): #function based view
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, "notepad/create.html", context)