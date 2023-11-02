from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.users.views import CustomUserDetailsView


# TODO: Change "Core"
schema_view = get_schema_view(
    openapi.Info(
        title="Core",
        default_version="v1.0",
        description="Core endpoints",
        contact=openapi.Contact(email="core@mail.com"), 
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Documentation
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),

    # Admin Panel
    path(settings.ADMIN_URL, admin.site.urls),
    
    # User
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/v1/auth/user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path( "api/v1/auth/password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

]

# TODO: Change "Core"
admin.site.site_header = "Core Admin"
admin.site.site_title = "Core Admin Portal"
admin.site.index_title = "Welcome to Core Portal"