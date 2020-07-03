from .models import *
from accounts.models import *
from django import forms

class AddLevelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Level
        fields = ['name',]

    def checkDuplicate(self):
        level_name = self.cleaned_data.get('name')
        qs = Level.objects.filter(name=level_name)
        if qs.exists():
            raise forms.ValidationError("Level Already Exist")
        return level_name
    
    def save(self, commit=True):
        level = super(AddLevelForm, self).save(commit=False)
        level.name = self.checkDuplicate()
        if commit:
            level.save()
        return level

class AddClassRoomForm(forms.ModelForm):
    room_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),min_value=0)
    class Meta:
        model = ClassRoom
        exclude = [
            'level',
            'incharge'
        ]

    def checkDuplicate(self):
        room_number = self.cleaned_data.get('room_number')
        qs = ClassRoom.objects.filter(pk=room_number)
        if qs.exists():
            raise forms.ValidationError("This class room is taken")
        return room_number
    
    def save(self, commit=True):
        class_room = super(AddClassRoomForm, self).save(commit=False)
        class_room.room_number = self.checkDuplicate()
        section = self.cleaned_data.get('section')
        student_capacity = self.cleaned_data.get('student_capacity')
        if commit:
            level.save()
        return level


