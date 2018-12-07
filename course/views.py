from django.urls import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from course.forms import StudentForm
from course.models import Student


def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

    def get_success_url(self):
        return reverse('course:list_students')


class StudentEdit(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

    def get_success_url(self):
        return reverse('course:list_students')
