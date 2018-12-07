from django.urls import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from course.forms import StudentForm
from course.models import Student
# from


# @login_required
def home(request):
    return render(request, 'home.html')

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
    template_name = 'edit_student.html'

    def get_success_url(self):
        return reverse('course:list_students')


class StudentDelete(DeleteView):
    model = Student
    form_class = StudentForm
    template_name = 'delete_student.html'

    def get_context_data(self, **kwargs):
        context_data = super(StudentDelete, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        student = Student.objects.get(id=int(pk))
        context_data.update({'student': student})
        return context_data

    def get_success_url(self):
        return reverse('course:list_students')
