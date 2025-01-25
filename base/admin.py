from django.contrib import admin
from .models import StudentProfile, Quiz, Submission, Courses, StudentComplaints

admin.site.register(StudentProfile)
admin.site.register(Quiz)
admin.site.register(Submission)
admin.site.register(Courses)
admin.site.register(StudentComplaints)