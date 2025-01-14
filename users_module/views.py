from rest_framework.viewsets import ModelViewSet
from models import User
from serializers import UserSerializer
from rest_framework.decorators import action


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer(partial=True)

    @action(detail=False, methods=['post'], url_path='register')
    def create_user(self, request):
        return self.create(request)
