from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from accounts.forms import *
from django.utils.html import escape

def home(request):
    return render(request, 'campus/home.html')

class AddLevel(View):
    template_name = 'campus/add_level.html'
    def get(self, request):
        form =  AddLevelForm(request.POST or None)
        context = { 'form': form }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AddLevelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('campus:levels')
        else:
            msg = 'Level already exists'
            return render(request, self.template_name,{'form':form, 'msg': msg})

class Levels(View):
    template_name = 'campus/levels.html'
    def get(self, request):
        levels = Level.objects.all()
        context = { 'levels': levels }
        return render(request, self.template_name, context)

class ClassRooms(View):
    template_name = 'campus/class_rooms.html'
    def get(self, request):
        class_rooms = ClassRoom.objects.all()
        context = { 'class_rooms': class_rooms }
        return render(request, self.template_name, context)

class AddClassRoom(View):
    template_name = 'campus/add_class_room.html'
    def get(self, request):
        form =  AddClassRoomForm(request.POST or None)
        context = { 'form': form }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AddClassRoomForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('campus:class_rooms')
        else:
            return render(request, self.template_name, {'form':form})
