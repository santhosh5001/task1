# urls.py
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import BranchListView, StudentListView, LectureListView

schema_view = get_schema_view(
    openapi.Info(
        title="Engineering College API",
        default_version='v1',
        description="API documentation for Engineering College",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/branches/', BranchListView.as_view(), name='branch-list'),
    path('api/students/', StudentListView.as_view(), name='student-list'),
    path('api/lectures/', LectureListView.as_view(), name='lecture-list'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
