from django.contrib import admin

from campus.models import (
    HrStaffAttendance, TeacherAttendance, ParentCalledForPTM, TeacherCalledForPTM, ClassRoom, StudentAttendance,
    Level, PTM, ClassRoomStudents, StudentLeave, Subject, SubjectTeachers, LevelSubjectTeacher, Period,
    TimeTable, SyllabusPlanning, DailyDiary,Assignment,AssignmentResult, Exam, ExamResult, ParentComplaint, StudentComplaint, Fine, Fee, 
    Event, EventInvites
)

class HrStaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('hrStaff', 'date', 'status')
admin.site.register(HrStaffAttendance, HrStaffAttendanceAdmin)
class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'date', 'status')
admin.site.register(TeacherAttendance, TeacherAttendanceAdmin)
class PTMAdmin(admin.ModelAdmin):
    list_display = ('id', 'agenda', 'manager', 'dateTime')
admin.site.register(PTM,  PTMAdmin)
class ParentCalledForPTMAdmin(admin.ModelAdmin):
    list_display = ('ptm', 'parent' )
admin.site.register(ParentCalledForPTM, ParentCalledForPTMAdmin)
class TeacherCalledForPTMAdmin(admin.ModelAdmin):
    list_display = ('ptm', 'teacher')
admin.site.register(TeacherCalledForPTM, TeacherCalledForPTMAdmin)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'level', 'section','student_capacity', 'incharge')
admin.site.register(ClassRoom, ClassRoomAdmin)
class ClassRoomStudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_room', 'student', 'session')
admin.site.register(ClassRoomStudents, ClassRoomStudentsAdmin)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'date', 'status')
admin.site.register(StudentAttendance, StudentAttendanceAdmin)
class PeriodAdmin(admin.ModelAdmin):
    list_display=('period', 'start_time', 'end_time')
admin.site.register(Period, PeriodAdmin)
class SubjectAdmin(admin.ModelAdmin):
    list_display=('id', 'name')
admin.site.register(Subject, SubjectAdmin)
class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display=('id', 'subject', 'teacher')
admin.site.register(SubjectTeachers, SubjectTeacherAdmin)
class LstAdmin(admin.ModelAdmin):
    list_display=('id', 'subject_teacher', 'level')
admin.site.register(LevelSubjectTeacher, LstAdmin)
class TimeTableAdmin(admin.ModelAdmin):
    list_display=('id', 'level_subject_teacher', 'class_room', 'period')
admin.site.register(TimeTable, TimeTableAdmin)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('id', 'level_subject_teacher', 'period_wise_content')
admin.site.register(SyllabusPlanning, SyllabusAdmin)
class StudentComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'detail', 'teacher')
admin.site.register(StudentComplaint, StudentComplaintAdmin)
class StudentLeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'student', 'detail', 'from_date', 'to_date')
admin.site.register(StudentLeave, StudentLeaveAdmin)
class DailyDiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time_table', 'lesson_taught')
admin.site.register(DailyDiary, DailyDiaryAdmin)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'fee', 'event_manager')
admin.site.register(Event, EventAdmin)
class EventInvitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'parent')
admin.site.register(EventInvites, EventInvitesAdmin)
class FineAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_complaint', 'hrStaff', 'title', 'amount')
admin.site.register(Fine, FineAdmin)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'hrStaff', 'student', 'fine', 'current_month_fee', 'fee_status' ,'fee_deposit_date','fee_month')
admin.site.register(Fee, FeeAdmin)
admin.site.register(Level)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date_time', 'level_subject_teacher', 'class_room')
admin.site.register(Assignment, AssignmentAdmin)
class AssignmentResultAdmin(admin.ModelAdmin):
    list_display= ('id', 'assignment', 'student', 'subject' , 'obtained_marks')
admin.site.register(AssignmentResult, AssignmentResultAdmin)

class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_time', 'subject', 'level')
admin.site.register(Exam, ExamAdmin)
class ExamResultAdmin(admin.ModelAdmin):
    list_display= ('id', 'exam', 'student', 'total_marks' , 'obtained_marks')
admin.site.register(ExamResult, ExamResultAdmin)
class ParentComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent','date', 'detail', 'status')
admin.site.register(ParentComplaint, ParentComplaintAdmin)
