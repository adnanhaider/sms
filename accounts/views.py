from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout,  update_session_auth_hash, get_user_model
User = get_user_model()
from django.contrib.auth.models import Group
from .forms import *
from campus.models import *
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from .minxins import *

class ProfileView(View):
    template_name = 'accounts/user/profile.html'
    def get(self, request):
        context = { 'user': request.user }
        return render(request, self.template_name, context)

class EditProfileView(View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        context = {'form' : form }
        return render(request, 'accounts/user/editProfile.html', context)
    def post(self, request):
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:profile'))

class CreatePrincipalUser(View):
    template_name = 'accounts/principal/createPrincipal.html'
    def get(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = PrincipalProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        context = {'form':user_form, 'address_form': address_form, 'profile_form':profile_form}
        return render(request, self.template_name , context)

    def post(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = PrincipalProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        if request.method == 'POST':
            if user_form.is_valid() and address_form.is_valid() and profile_form.is_valid():
                user_instance = user_form.save()
                if len(Group.objects.all()) == 0:
                    Group.objects.create(name='Principal')
                    Group.objects.create(name='Hr')
                    Group.objects.create(name='Teacher')
                    Group.objects.create(name='Parent')
                    Group.objects.create(name='Student')
                user_instance.groups.add(Group.objects.get(name='Principal'))
                address_instance = address_form.save()
                Principal.objects.create(
                    user=user_instance,
                    gender = profile_form.cleaned_data.get('gender'),
                    photo = self.request.FILES.get('photo'),
                    birth_date = profile_form.cleaned_data.get('birth_date'),
                    date_left = profile_form.cleaned_data.get('date_left'),
                    salary = profile_form.cleaned_data.get('salary'),
                    contact_number = profile_form.cleaned_data.get('contact_number'),
                    address = address_instance,
                )
                return redirect('accounts:view_principal',)

class CreateHrUser(View):
    def get(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = HrProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        context = {'form':user_form, 'address_form': address_form, 'profile_form':profile_form}
        return render(request, 'accounts/hr/createHr.html', context)
    def post(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = HrProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        if request.method == 'POST':
            if user_form.is_valid() and address_form.is_valid() and profile_form.is_valid():
                user_instance = user_form.save()
                if len(Group.objects.all()) == 0:
                    Group.objects.create(name='Principal')
                    Group.objects.create(name='Hr')
                    Group.objects.create(name='Teacher')
                    Group.objects.create(name='Parent')
                    Group.objects.create(name='Student')
                user_instance.groups.add(Group.objects.get(name='Hr'))
                address_instance = address_form.save()
                HrStaff.objects.create(
                    user=user_instance,
                    gender = profile_form.cleaned_data.get('gender'),
                    photo = self.request.FILES.get('photo'),
                    birth_date = profile_form.cleaned_data.get('birth_date'),
                    date_left = profile_form.cleaned_data.get('date_left'),
                    salary = profile_form.cleaned_data.get('salary'),
                    contact_number = profile_form.cleaned_data.get('contact_number'),
                    address = address_instance,
                )
                return redirect('accounts:view_hr',)

class CreateTeacherUser(View):
    def get(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = TeacherProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        context = {'form':user_form, 'address_form': address_form, 'profile_form':profile_form}
        return render(request, 'accounts/teacher/createTeacher.html', context)
    def post(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = TeacherProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        context = {'form':user_form, 'address_form': address_form, 'profile_form':profile_form}
        if request.method == 'POST':
            if user_form.is_valid() and address_form.is_valid() and profile_form.is_valid():
                user_instance = user_form.save()
                if len(Group.objects.all()) == 0:
                    Group.objects.create(name='Principal')
                    Group.objects.create(name='Hr')
                    Group.objects.create(name='Teacher')
                    Group.objects.create(name='Parent')
                    Group.objects.create(name='Student')
                user_instance.groups.add(Group.objects.get(name='Teacher'))
                address_instance = address_form.save()
                Teacher.objects.create(
                    user=user_instance,
                    gender = profile_form.cleaned_data.get('gender'),
                    photo = self.request.FILES.get('photo'),
                    birth_date = profile_form.cleaned_data.get('birth_date'),
                    date_left = profile_form.cleaned_data.get('date_left'),
                    salary = profile_form.cleaned_data.get('salary'),
                    contact_number = profile_form.cleaned_data.get('contact_number'),
                    address = address_instance,
                )
                return redirect('accounts:view_teacher',)
            else:
                return render(request, 'accounts/teacher/createTeacher.html', context)

class CreateParentUser(View):
    def get(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = ParentProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        context = {'form':user_form, 'address_form': address_form, 'profile_form':profile_form}
        return render(request, 'accounts/parent/createParent.html', context)
    def post(self, request):
        user_form = RegisterForm(request.POST or None)
        profile_form = ParentProfileForm(request.POST or None)
        address_form = AddressForm(request.POST or None)
        context = {'form':user_form, 'address_form': address_form, 'profile_form':profile_form}
        if request.method == 'POST':
            if user_form.is_valid() and address_form.is_valid() and profile_form.is_valid():
                user_instance = user_form.save()
                if len(Group.objects.all()) == 0:
                    Group.objects.create(name='Principal')
                    Group.objects.create(name='Hr')
                    Group.objects.create(name='Teacher')
                    Group.objects.create(name='Parent')
                    Group.objects.create(name='Student')
                user_instance.groups.add(Group.objects.get(name='Parent'))
                address_instance = address_form.save()
                Parent.objects.create(
                    user=user_instance,
                    gender = profile_form.cleaned_data.get('gender'),
                    photo = self.request.FILES.get('photo'),
                    birth_date = profile_form.cleaned_data.get('birth_date'),
                    contact_number = profile_form.cleaned_data.get('contact_number'),
                    address = address_instance,
                )
                return redirect('accounts:view_parent')
            else:
                return render(request,'accounts/parent/createParent.html', context)

class CreateStudentUser(View):
    def getStudentCountInClass(self, class_room):
        class_rooms_students = ClassRoomStudents.objects.all()
        count = 0
        for class_room_students in class_rooms_students:
            if class_room_students.class_room == class_room:
                count = count + 1
        return count
    def getTotalStudentCount(self):
        return Student.objects.all().count()
    def get(self, request):
        std_user_form = RegisterForm(request.POST or None)
        std_profile_form = StudentProfileForm(request.POST or None)
        parents = Parent.objects.all()
        class_rooms = ClassRoom.objects.all()
        class_rooms_with_student_count_dictionary = {}
        for class_room in class_rooms:
            class_rooms_with_student_count_dictionary.update(
                {class_room: { self.getStudentCountInClass(class_room) : class_room.student_capacity}})
        
        context = {
            'std_user_form': std_user_form,
            'std_profile_form': std_profile_form,
            'parents': parents,
            'class_rooms_with_student_count_dictionary': class_rooms_with_student_count_dictionary
        }
        return render(request, 'accounts/student/createStudent.html', context)

    def post(self, request):
        std_user_form = RegisterForm(request.POST or None)
        std_profile_form = StudentProfileForm(request.POST or None)
        parents = Parent.objects.all()
        class_rooms = ClassRoom.objects.all()
        class_rooms_with_student_count_dictionary = {}
        for class_room in class_rooms:
            class_rooms_with_student_count_dictionary.update(
                {class_room: {self.getStudentCountInClass(class_room): class_room.student_capacity}})
        context = {
            'std_user_form': std_user_form,
            'std_profile_form': std_profile_form,
            'parents': parents,
            'class_rooms_with_student_count_dictionary': class_rooms_with_student_count_dictionary
        }
        
        if std_user_form.is_valid() and std_profile_form.is_valid():
            std_user_instance = std_user_form.save()
            if len(Group.objects.all()) == 0:
                Group.objects.create(name='Principal')
                Group.objects.create(name='Hr')
                Group.objects.create(name='Teacher')
                Group.objects.create(name='Parent')
                Group.objects.create(name='Student')
            std_user_instance.groups.add(Group.objects.get(name='Student'))
            parent_obj = request.POST.get('guardian')
            class_room_obj = request.POST.get('class_room')
            std_instance = Student.objects.create(
                user=std_user_instance,
                gender = std_profile_form.cleaned_data.get('gender'),
                photo = self.request.FILES.get('photo'), 
                birth_date = std_profile_form.cleaned_data.get('birth_date'),
                reg_number = str(datetime.datetime.now().year-2000)+
                    str(datetime.datetime.now().month)+
                    str(101+self.getTotalStudentCount()),
                roll_number = 1, # temporarily giving 1 roll_number and updating again to the number of students in the class
                status = 'A', # student will be active on creation and Inactive only when passed out of left school
                guardian = get_object_or_404(Parent, id=parent_obj)
            )
            student_class_room = ClassRoomStudents.objects.create(
                class_room = get_object_or_404(ClassRoom, pk=class_room_obj),

                student = get_object_or_404(Student, pk=std_instance.reg_number),
                session = datetime.datetime.now().year
            )
            Student.objects.filter(user=std_user_instance).update(
                roll_number = self.getStudentCountInClass(student_class_room.class_room)
            )
            return redirect('accounts:view_student')
        else:
            return render(request, 'accounts/student/createStudent.html', context)

class ViewPrincipalUser(View):
    template_name = 'accounts/principal/principals.html'
    def get(self, request):
        principals = Principal.objects.all()
        context = { 'principals': principals }
        return render(request, self.template_name, context)

class ViewHrUser(View):
    template_name = 'accounts/hr/hrs.html'
    def get(self, request):
        hrs = HrStaff.objects.all()
        context = { 'hrs': hrs }
        return render(request, self.template_name, context)

class ViewTeacherUser(View):
    template_name = 'accounts/teacher/teachers.html'
    def get(self, request):
        teachers = Teacher.objects.all()
        context = { 'teachers': teachers }
        return render(request, self.template_name, context)

class ViewParentUser(View):
    template_name = 'accounts/parent/parents.html'
    def get(self, request):
        parents = Parent.objects.all()
        context = { 'parents': parents }
        return render(request, self.template_name, context)

class ViewStudentUser(View):
    template_name = 'accounts/student/students.html'
    def get(self, request):
        students = Student.objects.all()
        class_room_students = ClassRoomStudents.objects.all()
        context = { 'students': students, 'class_room_students':class_room_students}
        return render(request, self.template_name, context)


class PrincipalIndexView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/principal/index.html', context)

class HrIndexView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/hr/index.html', context)

class TeacherIndexView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/teacher/index.html', context)

class ParentIndexView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/parent/index.html', context)

class StudentIndexView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/student/index.html', context)

class ApproveTeacherView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/principal/approve_teacher.html', context)

class ApproveParentView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/principal/approve_parent.html', context)

class ApproveStudentView(View):
    def get(self, request):
        context={}
        return render(request, 'accounts/principal/approve_student.html', context)

