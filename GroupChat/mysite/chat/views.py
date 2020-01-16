#******************************************************************************************************************
# @purpose :Creating GroupChat Application.
# @file  :view.py
# @author :ShalineeBhawnani
#*******************************************************************************************************************
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })