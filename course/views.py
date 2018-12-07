from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from course.forms import StudentForm
from course.models import Student
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator


@login_required
def home(request):
    user = request.user
    if user.is_superuser:
        return render(request, 'home_admin.html')
    elif user.has_perm('course.is_teacher'):
        return redirect(reverse('course:home_teacher'))
    elif user.has_perm('course.is_student'):
        return redirect(reverse('course:home_student'))
    else:
        return render(request, 'home.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def home_admin(request):
    return render(request, 'home_admin.html')

@permission_required('course.is_teacher')
def home_teacher(request):
    return render(request, 'home_teacher.html')

@permission_required('course.is_student')
def home_student(request):
    return render(request, 'home_student.html')

@login_required
# @permission_required('course.is_teacher')
def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})


@method_decorator(login_required, name='dispatch')
class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

    def get_success_url(self):
        return reverse('course:list_students')


@method_decorator(login_required, name='dispatch')
class StudentEdit(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit_student.html'

    def get_success_url(self):
        return reverse('course:list_students')


@method_decorator(login_required, name='dispatch')
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


class ListSubjects(ListView):
    template_name = 'home_teacher.html'
    model = Student

    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        student = Student.objects.get(name=name)
        subjects = student.subject_student.all()
        data = serializers.serialize('json', subjects, fields=('name, credits'))
        return HttpResponse(data, content_type='application/json')
