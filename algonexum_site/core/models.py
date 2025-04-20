from django.db import models

# Create your models here.


class User(models.Model):
    fullname = models.CharField(max_length=254)
    email = models.EmailField(unique=True,max_length=254)
    password = models.CharField(max_length=254)
    def __str__(self):
        return self.fullname
    
class Course(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.user.username    
    

    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.course.title} - {self.title}"
    