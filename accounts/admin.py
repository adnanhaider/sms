from django.contrib import admin
from django.contrib.auth import get_user_model
User = get_user_model()

from .forms import UserAdminCreationForm, UserAdminChangeForm, ParentProfileForm, StudentProfileForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import (
    Address, Principal, HrStaff, Teacher, Parent, Student
    )
from .sites import accounts_admin_site
class StudentModelAdmin(admin.ModelAdmin):
    form = StudentProfileForm
accounts_admin_site.register(Parent, admin.ModelAdmin)
accounts_admin_site.register(Student,StudentModelAdmin)


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'first_name','last_name')
    list_filter = ('groups',)
    # this fieldsets is for changing/editing a user
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'groups' )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets is for adding new user data
    add_fieldsets = (
        (
            None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'groups', )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)
    filter_horizontal = ()
admin.site.register(User, UserAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('house_number', 'street_number', 'city')
admin.site.register(Address, AddressAdmin)

class PrincipalAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'contact_number', 'photo')
admin.site.register(Principal, PrincipalAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'contact_number', 'photo')
admin.site.register(Teacher, TeacherAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'contact_number', 'photo')
admin.site.register(Parent, ParentAdmin)

class HRAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'contact_number')
admin.site.register(HrStaff, HRAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number',)
admin.site.register(Student, StudentAdmin)
