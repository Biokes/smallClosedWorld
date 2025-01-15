from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users_module.views import RegisterView

# router = DefaultRouter()
# router.register(r'users', RegisterView.as_view(), name='register')

urlpatterns = [
    # path('/', include(router.urls)),
    path('auth/register', RegisterView.as_view(), name='register')
    # path('register/', UserViewSet.as_view({'post': 'create'}), name='register-user'),
]
