from django import forms
from course.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-crontrol'}),
            'last_name': forms.TextInput(attrs={'class': 'form-crontrol'}),
            'subject_student': forms.SelectMultiple(attrs={'class': 'form-crontrol'}),
        }
