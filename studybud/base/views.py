from django.shortcuts import render

rooms = [{'id':1, 'name': 'learn python'}, {'id':2, 'name': 'design'}, {'id':3, 'name': 'frontend'}, ]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'rooms':rooms})

def room(request, id):
    room = None
    for room in rooms:
        if room['id'] == int(id):
            render_room = room
    context = {'room': render_room}
    return render(request, 'room.html', context)
