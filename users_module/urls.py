from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users_module.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('/', include(router.urls)),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='register-user'),
]
