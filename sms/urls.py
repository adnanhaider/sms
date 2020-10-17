
from django.contrib import admin
from django.urls import path, reverse_lazy, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_redirect, name = 'login_redirect'),
    path('account/', include('accounts.urls', namespace='accounts')),
    path('campus/', include('campus.urls', namespace='campus')),

    path('password_change/', PasswordChangeView.as_view(template_name='passwords/change_password.html',
    success_url = reverse_lazy('password_change_done')), name='password_change'),

    path('password_change/done/', PasswordChangeDoneView.as_view
    (template_name='passwords/password_change_done.html'), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view
    (
        template_name='passwords/password_reset_form.html',
        email_template_name='passwords/password_reset_email.html',
        subject_template_name = 'passwords/password_reset_subject.txt',
        success_url = reverse_lazy('password_reset_done')
    ),
     name='password_reset'),

    path('password_reset/done/', PasswordResetDoneView.as_view
    (template_name='passwords/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view
    (template_name='passwords/password_reset_confirm.html',
    success_url = reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    
    path('reset/done/', PasswordResetCompleteView.as_view
    (template_name='passwords/password_reset_complete.html'), name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)