from django.contrib import admin
from .models import Student, Subject


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'credits')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
