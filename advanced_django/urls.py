from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from course import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.urls'), name='couse'),
]
# + static(BASE_DIR.settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
