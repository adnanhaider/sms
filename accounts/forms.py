from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *
from campus.models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
    ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.clean_email()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AddressForm(forms.ModelForm):
    house_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    street_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    town = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Address
        fields = '__all__'

    def save(self, commit=True):
        address = super(AddressForm, self).save(commit=False)
        address.house_number = self.cleaned_data['house_number']
        address.street_number = self.cleaned_data['street_number']
        address.town = self.cleaned_data['town']
        address.city = self.cleaned_data['city']
        address.state = self.cleaned_data['state']
        if commit:
            address.save()
        return address

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False)
    birth_date = forms.DateField(widget=DateInput())
    salary = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control','min':0}), required=False)
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'selectpicker form-control', 'title': 'Select Gender'}), 
        choices=CHOICES)
    
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    class Meta:
        model = Profile
        fields = [
            'gender',
            'photo',
            'birth_date',
            'salary',
            'contact_number',
        ]
        widgets = {'birth_date': DateInput()}

class PrincipalProfileForm(ProfileForm):
    class Meta:
        model = Principal
        exclude = ( 'user', 'address',)

class HrProfileForm(ProfileForm):
    class Meta:
        model = HrStaff
        exclude = ('user', 'address',)

class TeacherProfileForm(ProfileForm):
    class Meta:
        model = Teacher
        exclude = ( 'user', 'address',)

class StudentProfileForm(ProfileForm):
    class Meta:
        model = Student
        exclude = ['user', 'guardian','salary', 'date_left', 'contact_number', 'status', 'reg_number', 'roll_number']

class ParentProfileForm(ProfileForm):
    class Meta:
        model = Parent
        exclude = ( 'user', 'address', 'salary' )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password','first_name', 'last_name', 'groups')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

