from django.urls import path
from users_module.views import RegisterView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register-user'),
]