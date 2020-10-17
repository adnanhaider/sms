
from django.urls import path
from . import views
app_name = 'campus'
urlpatterns = [
    path('', views.home),
    path('add-level/', views.AddLevel.as_view(), name='add_level'),
    path('levels/', views.Levels.as_view(), name='levels'),
    path('add-class-room/', views.AddClassRoom.as_view(), name='add_class_room'),
    path('class-rooms/', views.ClassRooms.as_view(), name='class_rooms'),
    path('make-hr-attendance/', views.HrAttendance.as_view(), name='make_hr_attendance'),
    # path('todays-hr-attendance/', views.TodaysHrAttendance.as_view(), name='todays_hr_attendance'),
    path('get-hr-attendance/', views.GetHrAttendance.as_view(), name='get_hr_attendance'),
    path('get-teacher-attendance/', views.GetTeacherAttendance.as_view(), name='get_teacher_attendance'),
    path('get-student-attendance/', views.GetStudentAttendance.as_view(), name='get_student_attendance'),
]
