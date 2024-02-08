# EngineeringCollege/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api.views import BranchListView, StudentListView, LectureListView  # Make sure to import your views

# Define your app-specific URL patterns
app_patterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),  # Use 'branches/' instead of 'api/branches/'
    path('students/', StudentListView.as_view(), name='student-list'),
    path('lectures/', LectureListView.as_view(), name='lecture-list'),
    # ... other app-specific URL patterns
]


# Define authentication-related URL patterns
auth_patterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Define Swagger documentation views
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
)

# Extend the urlpatterns list with your app-specific and authentication patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your app-specific patterns
    path('api/', include(app_patterns)),
    # Include authentication-related patterns
    path('api/auth/', include(auth_patterns)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Ensure that BranchListView, StudentListView, and LectureListView are imported at the beginning of the file
# Example:
# from api.views import BranchListView, StudentListView, LectureListView
