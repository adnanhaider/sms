from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from accounts.forms import *
from django.utils.html import escape

def home(request):
    return render(request, 'campus/home.html')

class AddLevel(View):
    template_name = 'campus/level/add_level.html'
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
    template_name = 'campus/level/levels.html'
    def get(self, request):
        levels = Level.objects.all()
        context = { 'levels': levels }
        return render(request, self.template_name, context)

class ClassRooms(View):
    template_name = 'campus/class_room/class_rooms.html'
    def get(self, request):
        class_rooms = ClassRoom.objects.all()
        context = { 'class_rooms': class_rooms }
        return render(request, self.template_name, context)

class AddClassRoom(View):
    template_name = 'campus/class_room/add_class_room.html'
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

class HrAttendance(View):
    template_name = 'campus/attendance/make_hr_attendance.html'
    def get(self, request):
        form = AddHrAttendanceForm(request.POST or None)
        hr_list = HrStaff.objects.all() 
        dateToday = datetime.date.today
        context = {'form': form, 'hr_list': hr_list, 'date': dateToday}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AddHrAttendanceForm(request.POST or None)
        hr_list = HrStaff.objects.all()
        dateToday = datetime.date.today
        context = {'form': form, 'hr_list': hr_list, 'date':dateToday}
        # print(form.is_valid())
        # print('------------------------------')
        if form.is_valid():
            for hr in hr_list:
                obj = HrStaffAttendance.objects.create(
                    hrStaff=hr.user,
                    status=form.cleaned_data.get('status').filter(form.hrStaff==hr.user),
                    date=dateToday
                )
            form.save()
            return redirect('campus:todays_hr_attendance')
        else:
            return render(request, self.template_name, context)

# class TodaysHrAttendance(View):
#     template_name = 'campus/attendance/make_hr_attendance.html'
#     def get(self, request):
#         form = AddHrAttendanceForm(request.POST or None)
#         hr_list = HrStaff.objects.all()
#         dateToday = datetime.date.today
#         hr_attendance_list = HrStaffAttendance.objects.filter(date=datetime.datetime.now)
#         context = {'form': form, 'hr_list': hr_attendance_list, 'date':dateToday}
#         return render(request, self.template_name, context)

class GetHrAttendance(View):
    template_name = 'campus/attendance/get_hr_attendance.html'
    def get(self, request):
        form = AddHrAttendanceForm(request.POST or None)
        hr_list = HrStaff.objects.all()
        dateToday = datetime.date.today
        context = {'form': form, 'hr_list': hr_list, 'date':dateToday}
        return render(request, self.template_name, context)

class GetTeacherAttendance(View):
    template_name = 'campus/attendance/get_hr_attendance.html'
    def get(self, request):
        form = AddHrAttendanceForm(request.POST or None)
        hr_list = HrStaff.objects.all()
        dateToday = datetime.date.today
        context = {'form': form, 'hr_list': hr_list, 'date':dateToday}
        return render(request, self.template_name, context)

class GetStudentAttendance(View):
    template_name = 'campus/attendance/get_hr_attendance.html'
    def get(self, request):
        form = AddHrAttendanceForm(request.POST or None)
        hr_list = HrStaff.objects.all()
        dateToday = datetime.date.today
        context = {'form': form, 'hr_list': hr_list, 'date':dateToday}
        return render(request, self.template_name, context)

