from django.shortcuts import render

rooms = [{'id':1, 'name': 'learn python'}, {'id':2, 'name': 'design'}, {'id':3, 'name': 'frontend'}, ]

# Create your views here.
def home(request):
    return render(request, 'home.html', {'rooms':rooms})

def room(request):
    return render(request, 'room.html')
