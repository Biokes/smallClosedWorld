from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

# from users_management.views import RegisterView

# router = DefaultRouter()
# router.register(r'users', RegisterView.as_view(), name='register')


urlpatterns = [
    path('auth/register', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # Djoser JWT support
    path('auth/token/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/users/reset_password/', include('djoser.urls')),
    path('auth/users/reset_password/confirm/', include('djoser.urls')),
]
# /**
# POST /auth/users/: Register a new user.
# POST /auth/users/activation/: Activate a user account.
# POST /auth/users/reset_password/: Request a password reset.
# POST /auth/users/reset_password_confirm/: Confirm password reset.
# POST /auth/users/set_password/: Change the password for logged-in users.
# GET /auth/users/me/: Retrieve the profile of the currently logged-in user.
# PUT /auth/users/me/: Update the profile of the currently logged-in user.
# path('auth/users/resend_activation/', include('djoser.urls')),  # Resend activation email
#path('auth/users/set_password/', include('djoser.urls.password')),  # Set new password
#
# # Set new username (authenticated user)
# path('auth/users/set_username/', include('djoser.urls')),  # Set new username
#
# # Username reset endpoints
# path('auth/users/reset_username/', include('djoser.urls')),  # Reset username
# path('auth/users/reset_username/confirm/', include('djoser.urls')),  # Confirm username reset

# Current user (profile information)
# path('auth/users/me/', include('djoser.urls')),  # Get and update current user's profile
