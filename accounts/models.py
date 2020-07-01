from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from django.urls import reverse
from accounts.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True) 
       
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        db_table = "User"
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return self.get_full_name()
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
 
    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Address(models.Model):
    house_number = models.CharField(max_length=20)
    street_number = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    # def __str__(self):
    #     return self.city
    class Meta:
        db_table = 'Address'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='static/images/', null=True, blank=True)
    birth_date = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    salary = models.FloatField(max_length=6)
    contact_number = models.CharField(max_length=11)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.user.__str__()
        
    @property
    def getAge(self):
        return int(datetime.date.today() - self.birth_date)
    class Meta:
        abstract = True

class Principal(Profile):
    class Meta:
        db_table = 'Principal'
        verbose_name = _('principal')
        verbose_name_plural = _('principals')

    # def get_absolute_url(self):
    #     return reverse("accounts:principal", kwargs={'id':self.user.id}) 

    def logIn(self):
        return True

    def addNewHr(self, hr_obj):
        # code for adding new hr
        return True

    def approveStudentLeave(self, std_id):
        # code for leave
        return True

    def approveLeave(self, id):
        return True

    def approveAccount(self, id):
        # account id will show the details
        return True

    def callEvent(self):
        pass

    def viewProgress(self):
        pass

class HrStaff(Profile):
    class Meta:
        db_table = 'HrStaff'
        verbose_name = _('hr staff')
        verbose_name_plural = _('hr staff')

    def logIn(self):
        return True

    def updateStudentFee(self, std_id):
        return True

    def updateLevelFee(self, Level_id):
        return True

    def updateSalary(self, id):
        return True

    def addNewParent(self, parent_obj):
        return True

    def addNewStudent(self, std_obj):
        return True

    def addNewTeacher(self, teacher_obj):
        return True

    def addNewPeriod(self, tcl_id, classRoom_id, period_id):
        return True

    def setNotice(self, detail):
        return True

    def managePTM(self, parent_list, teacher_list, ptm_id):
        return True

    def fineStudent(self, std_id):
        return True

class Teacher(Profile):
    class Meta:
        db_table = 'Teacher'
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')

    def logIn(self):
        return True

    def makeClassRoomAttendance(self, classRoom_id):
        return True

    def addNewExam(self, exam_obj):
        return True

    def addNewResult(self, result_obj):
        return True

    def requestPTM(self, parent_list):
        return True

    def updateDailyDiary(self, dailyDairy_obj):
        return True

    def setSyllabusPlanning(self, syllabusPlanning_obj):
        return True

    def makeStudentComplaint(self, std_id):
        return True

class Parent(Profile):
    salary = None
    date_left = None
    
    class Meta:
        db_table = 'Parent'
        verbose_name = _('parent')
        verbose_name_plural = _('parents')
        

    def logIn(self):
        return True

    def viewResult(self, std_id):
        return True

    def applyLeave(self, std_id):
        return True

    def requestPTM(self, teacher_list):
        return True

    def makeSuggComplaint(self, detail):
        return True

    def applySLC(self, std_id):
        return True

class Student(Profile):
    salary = None
    contact_number = None
    address = None
    roll_number = models.PositiveIntegerField(primary_key=True, unique=True)
    STATUS_CHOICES = [('A', 'Active'), ('I', 'Inactive')]
    status = models.CharField(max_length=1, default='A', choices=STATUS_CHOICES)
    guardian = models.ForeignKey("Parent", on_delete=models.CASCADE)

    USERNAME_FIELD = 'roll_number'
    REQUIRED_FIELDS = []
    class Meta:
        db_table = 'Student'
        verbose_name = _('student')
        verbose_name_plural = _('students')

    def logIn(self):
        return True

    def viewResult(self):
        return True

    def uploadAssignment(self, exame_id):
        return True

    def checkAttendance(self):
        return True

