from django.conf.urls import include, url
from django.contrib import admin
from students import views
from rest_framework import routers
from students import views

router = routers.DefaultRouter()
router.register(r'student', views.StudentView,'student')
# from django.urls import path,re_path
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    # url(r'^api/students/$',views.student_list),
    # url(r'^api/students/([0-9])$',views.student_detail),
]
