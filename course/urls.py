from django.urls import path
from course import views

app_name = "course"
urlpatterns = [
    path('list_students/', views.list_students, name='list_students'),
    path('create_student/', views.StudentCreate.as_view(), name='create_student'),
    path('edit_student/<slug:pk>', views.StudentEdit.as_view(), name='edit_student'),
    path('delete/<slug:pk>', views.StudentDelete.as_view(), name='delete_student'),
]
