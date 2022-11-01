from django.shortcuts import render
from .models import Room

rooms = [{'id':1, 'name': 'learn python'}, {'id':2, 'name': 'design'}, {'id':3, 'name': 'frontend'}, ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms':rooms})

def room(request, id):
    room = Room.objects.get(id=id)
    # room = None
    # for room in rooms:
    #     if room['id'] == int(id):
    #         render_room = room
    context = {'room': room}
    return render(request, 'room.html', context)
