from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


rooms = [{'id':1, 'name': 'learn python'}, {'id':2, 'name': 'design'}, {'id':3, 'name': 'frontend'}, ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms':rooms})

def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'room_form.html', context)