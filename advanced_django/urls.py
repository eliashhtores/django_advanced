from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import login, logout_then_login
from course import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('course/', include('course.urls',namespace = 'course'), name='course'),
    path('login/', login, {'template_name': 'login.html'}, name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('subject/', include('course.urls',namespace = 'subject'), name='subject'),
    path('api-auth/', include('rest_framework.urls'), name='api-auth'),
]
# + static(BASE_DIR.settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
