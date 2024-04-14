from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from employee import views

router = routers.DefaultRouter()
router.register(r'employee', views.EmployeeView, 'Employee')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Employee API"))
]