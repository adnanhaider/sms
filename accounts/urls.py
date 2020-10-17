from django.urls import path, reverse_lazy
from accounts import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [ 
    path('login/',LoginView.as_view(template_name='accounts/user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/user/logged_out.html'), name='logout'),    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),

    path('create-principal/', views.CreatePrincipalUser.as_view(), name='create_principal'),
    path('create-hr/', views.CreateHrUser.as_view(), name='create_hr'),
    path('create-teacher/', views.CreateTeacherUser.as_view(), name='create_teacher'),
    path('create-parent/', views.CreateParentUser.as_view(), name='create_parent'),
    path('create-student/', views.CreateStudentUser.as_view(), name='create_student'),

    path('view-principal/', views.ViewPrincipalUser.as_view(), name='view_principal'),
    path('view-hr/', views.ViewHrUser.as_view(), name='view_hr'),
    path('view-teacher/', views.ViewTeacherUser.as_view(), name='view_teacher'),
    path('view-parent/', views.ViewParentUser.as_view(), name='view_parent'),
    path('view-student/', views.ViewStudentUser.as_view(), name='view_student'),

    path('principal-dashboard/', views.PrincipalIndexView.as_view(), name='principalIndex'),
    path('hr-dashboard/', views.HrIndexView.as_view(), name='hrIndex'),
    path('teacher-dashboard/', views.TeacherIndexView.as_view(), name='teacherIndex'),
    path('parent-dashboard/', views.ParentIndexView.as_view(), name='parentIndex'),
    path('student-dashboard/', views.StudentIndexView.as_view(), name='studentIndex'),

    # principal usecases urls
    path('approve-teacher/', views.ApproveTeacherView.as_view(), name='approve_teacher'),
    path('approve-student/', views.ApproveStudentView.as_view(), name='approve_student'),
    path('approve-parent/', views.ApproveParentView.as_view(), name='approve_parent'),


] 





































# from django.contrib.auth.views import (
#     LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,
#     PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#     )


# path('', IndexView.as_view(), name='index'),
#     path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
#     path('logout/', LogoutView.as_view(template_name='accounts/logout.html')),
#     path('change-password/', PasswordChangeView.as_view(template_name='accounts/change_password.html')),
#     path('change-password_done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html')),
#     path('password-reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html')),
#     path('passwrod-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')),
#     path('reset/<uid64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html')),
#     path('reset/done/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')),
