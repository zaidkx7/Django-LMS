from django.db import models
from django.contrib.auth.models import User
import os

def student_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    student_username = instance.student.username
    course_no = instance.course.course_no
    quiz_no = instance.quiz.quiz_no
    filename = f"{student_username}-{course_no}-{quiz_no}.{ext}"
    return os.path.join(f'{course_no}', filename)

class StudentProfile(models.Model):
    # Extending the user model with a student profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Courses(models.Model):
    course_title = models.CharField(max_length=200)
    course_no = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.course_title

class Quiz(models.Model):
    quiz_title = models.CharField(max_length=200)
    quiz_no = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    help_file = models.FileField(upload_to='help_files/', null=True, blank=True)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE,default=1)
    quiz_created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.quiz_title

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    file = models.FileField(upload_to=student_directory_path)
    submitted_at = models.DateTimeField(auto_now_add=True)
    marks = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.student.username} - {self.course.course_no} - {self.quiz.quiz_no}"

class StudentComplaints(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username