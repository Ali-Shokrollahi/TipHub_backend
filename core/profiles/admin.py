from django.contrib import admin
from .models import StudentProfile, TeacherProfile, StaffProfile


class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'username']


class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)
admin.site.register(StaffProfile, StaffProfileAdmin)
