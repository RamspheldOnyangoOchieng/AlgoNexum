from django.contrib import admin
from .models import Course,Lesson

# Register your models here.
class LessonInline(admin.TabularInline):  # or StackedInline
    model = Lesson
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)