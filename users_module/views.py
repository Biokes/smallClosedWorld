from rest_framework.viewsets import ModelViewSet
from users_module.models import User
from users_module.serializers import UserSerializer
from rest_framework.decorators import action


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer(partial=True)

    @action(detail=False, methods=['post'], url_path='register')
    def create_user(self, request):
        return self.create(request)
