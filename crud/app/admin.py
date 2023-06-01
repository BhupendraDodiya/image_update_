from django.contrib import admin
from .models import Student,Subject
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','subject','mobile','image','address']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject','fess','duration']