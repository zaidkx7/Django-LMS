from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Quiz, Submission, StudentComplaints


class QuizAddingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quiz_title'].required = True
        self.fields['quiz_no'].required = True
        self.fields['description'].required = True
        self.fields['due_date'].required = True
        self.fields['course'].required = True


        for field_name in self.fields:
            self.fields[field_name].help_text = ''

    class Meta:
        model = Quiz
        fields = "__all__"
        widgets = {
            "quiz_title": forms.TextInput(attrs={"class": "form-control"}),
            "quiz_no": forms.TextInput(attrs={"class": "form-control"}),
            "description": CKEditor5Widget(attrs={"class": "django_ckeditor_5", "config_name": "extends"}),
            "help_file": forms.FileInput(attrs={"class": "form-control"}),
            "due_date": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "course": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            "quiz_title": "Quiz Title",
            "quiz_no": "Quiz No",
            "description": "Quiz Description",
            "help_file": "Help File",
            "due_date": "Due Date",
            "course": "Course",
        }

class RemarksForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ["remarks"]
        widgets = {
            "remarks": CKEditor5Widget(attrs={"class": "django_ckeditor_5", "config_name": "extends"})
        }
        labels = {
            "remarks": "Remarks"
        }
    
class StudentComplaintsForm(forms.ModelForm):
    class Meta:
        model = StudentComplaints
        fields = ["complaint"]
        widgets = {
            "complaint": CKEditor5Widget(attrs={"class": "django_ckeditor_5", "config_name": "extends"})
        }
        labels = {
            "complaint": "Complaint"
        }