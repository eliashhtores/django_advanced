from django.urls import path
from course import views

app_name = "course"
urlpatterns = [
    path('list_students/', views.list_students, name='list_students'),
    path('create_student/', views.StudentCreate.as_view(), name='create_student'),
    path('edit_student/<slug:pk>', views.StudentEdit.as_view(), name='edit_student'),
    path('delete/<slug:pk>', views.StudentDelete.as_view(), name='delete_student'),
    path('home_teacher/', views.home_teacher, name='home_teacher'),
    path('home_student/', views.home_student, name='home_student'),
    path('home_admin/', views.home_admin, name='home_admin'),
    path('list_user_subjects/', views.ListSubjects.as_view(), name='list_user_subjects'),
]
