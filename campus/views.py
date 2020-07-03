from django.shortcuts import render, redirect
from django.views import View
from .forms import *

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
            # Level.objects.create(
            #     name = form.cleaned_data.get('name')
            # )
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

class AddClassRoom(View):
    template_name = 'campus/add_class_room.html'
    def get(self, request):
        form =  AddClassRoomForm(request.POST or None)
        context = { 'form': form }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AddLevelForm(request.POST or None)
        if form.is_valid():
            form.save()