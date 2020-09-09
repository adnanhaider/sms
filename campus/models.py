from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from accounts.models import HrStaff, Teacher, Parent, Student, Principal
from django.urls import reverse

class HrStaffAttendance(models.Model):
    hrStaff = models.ForeignKey(HrStaff, on_delete=models.CASCADE)
    date = models.DateField()
    STATUS_CHOICES = [('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    # def get_absolute_url(self):
    #     return reverse("campus:HrStaff-Attendance", kwargs={'id':id})
    def __str__(self):
        return '%s' % (self.status)

    class Meta: 
        db_table = 'HrStaffAttendance'
        unique_together = (('hrStaff', 'date'),)
        verbose_name = _('Hr Staff Attendance')
        verbose_name_plural = _('Hr Staff Attendance')

class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    STATUS_CHOICES = [('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'TeacherAttendance'
        unique_together = (('teacher', 'date'),)
        verbose_name = _('Teacher Attendance')
        verbose_name_plural = _('Teachers Attendance')

class PTM(models.Model):
    manager = models.ForeignKey(HrStaff, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
    agenda = models.TextField(max_length=1000)

    def __str__(self):
        return self.agenda
    class Meta:
        db_table = 'PTM'
        verbose_name = _('Parent Teacher Meeting')
        verbose_name_plural = _('Parent Teacher Meetings')

class ParentCalledForPTM(models.Model):
    ptm = models.ForeignKey(PTM, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'ParentCalledForPTM'
        unique_together = (('ptm', 'parent'),)
        verbose_name = _('Parents Called For Meeting')
        verbose_name_plural = _('Parents Called For Meetings')

class TeacherCalledForPTM(models.Model):
    ptm = models.ForeignKey(PTM, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TeacherCalledForPTM'
        unique_together = (('ptm', 'teacher'),)
        verbose_name = _('Teacher Called For Meeting')
        verbose_name_plural = _('Teachers Called For Meetings')

class Level(models.Model):
    name = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return '%s'%(self.name)

    class Meta:
        db_table = 'Level'
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')
  
class ClassRoom(models.Model):
    room_number = models.IntegerField(primary_key=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    section = models.CharField(max_length=30)
    student_capacity = models.IntegerField(default=30)
    incharge = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    def __str__(self):
        return '%s %s Room %s ' % (self.level, self.section, self.room_number)
    class Meta:
        db_table = "ClassRoom"
        verbose_name = _('Class Room')
        verbose_name_plural = _('Class Rooms')

class ClassRoomStudents(models.Model):
    class_room = models.ForeignKey(ClassRoom, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING )
    session = models.CharField(max_length=4, default=datetime.date.today().year) # hide this field using forms
    class Meta:
        unique_together = (('student', 'session'),)
        db_table = "ClassRoomStudents"
        verbose_name = _('Class Students')
        verbose_name_plural = _('Class Students')
   
class StudentAttendance(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Student")
    date = models.DateField()
    taken_by = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    STATUS_CHOICES = [('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return self.status

    class Meta: 
        db_table = 'StudentAttendance'
        unique_together = (('roll_number', 'date'),)
        verbose_name = _('Students Attendance')
        verbose_name_plural = _('Students Attendance')

class StudentLeave(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    detail = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()
    def __str__(self):
        return self.student
    class Meta:
        db_table = "StudentLeave"
        verbose_name = _('Student Leave')
        verbose_name_plural = _('Student Leaves')

class Subject(models.Model):
    '''
    This subject is just the names of subjects like English, Math, General Knowledge etc.
    '''
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Subject"
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

class SubjectTeachers(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def __str__(self):
        return ' %s | %s |' % (self.subject, self.teacher)
    class Meta:
        unique_together = ('subject', 'teacher'),
        db_table = "SubjectTeacher"
        verbose_name = _('Subject Teacher')
        verbose_name_plural = _('Subject Teachers')

class LevelSubjectTeacher(models.Model):
    subject_teacher = models.ForeignKey(SubjectTeachers, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete= models.CASCADE)
    def __str__(self):
        return 'Level %s | %s' % (self.level, self.subject_teacher)
    class Meta:
        unique_together = ('subject_teacher', 'level'),
        db_table = "LevelSubjectTeacher"
        verbose_name = _('Level Subject Teacher')
        verbose_name_plural = _('Level Subject Teachers')

class Period(models.Model):
    period = models.IntegerField(primary_key=True, default=1, validators=[MaxValueValidator(9), MinValueValidator(0)])
    # duration = models.DurationField(default=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        if self.period == 5:
            return 'Break'
        else:
            return 'period(%s)' % (self.period)
    class Meta:
        db_table = "Period"
        verbose_name = _('Period')
        verbose_name_plural = _('Periods')

class TimeTable(models.Model):
    level_subject_teacher = models.ForeignKey(LevelSubjectTeacher, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s' % (self.level_subject_teacher, self.class_room, self.period)
    class Meta:
        db_table = "TimeTable"
        unique_together = ('period', 'class_room'), ('class_room', 'level_subject_teacher')
        verbose_name = _('Time Table')
        verbose_name_plural = _('Time Tables')

class SyllabusPlanning(models.Model):
    level_subject_teacher = models.ForeignKey(LevelSubjectTeacher, on_delete=models.CASCADE)
    period_wise_content = models.TextField(max_length=1000)
    def __str__(self):
        return self.period_wise_content
    class Meta:
        db_table = "SyllabusPlanning"
        verbose_name = _('Syllabus Planning')
        verbose_name_plural = _('Syllabus Planning')

class DailyDiary(models.Model):
    date = models.DateField()
    time_table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    lesson_taught = models.TextField(max_length=1000)
    class Meta:
        db_table = "DailyDiary"
        unique_together = ('date', 'time_table'),
        verbose_name = _('Daily Diary')
        verbose_name_plural = _('Daily Diaries')

class Assignment(models.Model):
    title = models.CharField(max_length=30)
    assignment_file = models.FileField(null=True, blank=True)
    due_date_time = models.DateTimeField()
    level_subject_teacher = models.ForeignKey(LevelSubjectTeacher, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "Assignment"
        unique_together = (('title', 'class_room'),('title', 'level_subject_teacher'))
        verbose_name = _('Assignment')
        verbose_name_plural = _('Assignments')

class AssignmentResult(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    obtained_marks =models.FloatField()
    def __str__(self):
        return '%s %s %s' % (self.student, self.subject, self.obtained_marks)
    class Meta:
        db_table = "AssignmentResult"
        # unique_together = (('assignment', 'student'), ('student', 'subject'))
        verbose_name = _('Assignment Result')
        verbose_name_plural = _('Assignments Results')

class Exam(models.Model):
    name = models.CharField(max_length=30)
    date_time = models.DateTimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete = models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.name, self.subject)
    class Meta:
        db_table = "Exam"
        unique_together = (('date_time', 'level'), ('level', 'subject'))
        verbose_name = _('Exam')
        verbose_name_plural = _('Exams')

class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_marks = models.FloatField()
    obtained_marks = models.FloatField()
    def __str__(self):
        return '%s %s' % (self.subject, self.obtained_marks)
    class Meta:
        db_table = "ExamResult"
        verbose_name = _('Exam Result')
        verbose_name_plural = _('Exams Results')

class ParentComplaint(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    date = models.DateField()
    detail = models.TextField()
    STATUS_CHOICES = [('A', 'Addressed'), ('P', 'Pending')]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    def __str__(self):
        return '%s'% (self.parent)
    class Meta:
        db_table = "ParentComplaint"
        verbose_name = _('Parent Complaint')
        verbose_name_plural = _('Parent Complaints')
    
class StudentComplaint(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    detail = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)    
    def __str__(self):
        return '%s | by %s' % (self.detail, self.teacher)
    class Meta:
        db_table = "StudentComplaint"
        verbose_name = _('Student Complaint')
        verbose_name_plural = _('Student Complaints')

class Fine(models.Model):
    student_complaint = models.ForeignKey(StudentComplaint, on_delete=models.CASCADE)
    hrStaff = models.ForeignKey(HrStaff, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    amount = models.FloatField()
    def getTotalFile(self):
        '''
        amount variable will commulate the number of times student is fined into 
        amount of each fine
        '''
        return self.amount
    def __str__(self):
        return str(self.amount)
    class Meta:
        db_table = "Fine"
        verbose_name = _('Fine')
        verbose_name_plural = _('Fines')

class Fee(models.Model):
    hrStaff = models.ForeignKey(HrStaff, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fine = models.ForeignKey(Fine, on_delete=models.CASCADE, null=True, blank=True)
    current_month_fee = models.FloatField()
    STATUS_CHOICES = [('D', 'Due'), ('P', 'Paid')]
    fee_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='D')
    fee_deposit_date = models.DateField()
    fee_month = models.DateField(auto_now_add=True)
    class Meta:
        db_table = "Fee"
        verbose_name = _('Fee')
        verbose_name_plural = _('Fees')

class Event(models.Model):
    title = models.CharField(max_length=50, default='Sports Day')
    detail = models.TextField(default='')
    date = models.DateField()
    venue = models.CharField(max_length=50)
    fee = models.FloatField()
    event_manager = models.ForeignKey(HrStaff, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "Event"
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

class EventInvites(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.parent)
    class Meta:
        db_table = "EventInvites"
        unique_together = ('parent', 'event')
        verbose_name = _('Event Invites')
        verbose_name_plural = _('Event Invites')

    

