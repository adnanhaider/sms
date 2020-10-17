from .models import *
from accounts.models import *
from django import forms
from .widgets import *
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from .sites import campus_admin_site

class AddLevelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Level
        fields = ('name',)

class AddClassRoomForm(forms.ModelForm):
    room_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    section = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}),min_value=0)
    level = ClassRoom._meta.get_field('level').formfield(
            widget=RelatedFieldWidgetWrapper(
            ClassRoom._meta.get_field('level').formfield().widget,
            ClassRoom._meta.get_field('level').remote_field,
            campus_admin_site,
            can_add_related=True,
        )
    )
    incharge = ClassRoom._meta.get_field('incharge').formfield(
        widget=RelatedFieldWidgetWrapper(
            ClassRoom._meta.get_field('incharge').formfield().widget,
            ClassRoom._meta.get_field('incharge').remote_field,
            campus_admin_site,
            can_add_related=True,
        )
    )
    def __init__(self, *args, **kwargs):
        super(AddClassRoomForm, self).__init__(*args, **kwargs)
        self.fields['level'].widget.attrs.update({'class': 'custom-select-sm'})
        self.fields['incharge'].widget.attrs.update({'class':'custom-select-sm'})

    class Meta:
        model = ClassRoom
        fields = '__all__'
        
    def clean_room_number(self):
        room_number = self.cleaned_data.get('room_number')
        qs = ClassRoom.objects.filter(room_number=room_number)
        if qs.exists():
            raise forms.ValidationError('Room '+str(room_number) + ' is taken')
        return room_number
    
class AddHrAttendanceForm(forms.ModelForm):
    class Meta:
        model = HrStaffAttendance
        exclude = ['date']
        # fields = '__all__'

