from django.urls import path
from course import views

subject_data_list = views.SubjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

subject_data_detail = views.SubjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'create',
    'patch': 'partial_update',
    'delete': 'destroy',
})


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
    path('subject-data/', subject_data_list, name='subject-data-list'),
    path('subject-data/<slug:pk>', subject_data_detail, name='subject-data-detail'),
]
