from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from .models import User

class UserViewset(viewsets.ViewSet):
    """
    회원과 관련된 요청(회원가입, 로그인)을 수행하는 클래스
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """
        회원가입
        username : 5글자 이상
        pw : 8 글자 이상
        """
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as e:
            print(e)
            return Response(status=500)
        return Response(status=201)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        로그인
        email : '@' 포함
        pw : 8 글자 이상
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=request.data.get(
            'username'), password=request.data.get('password'))
        if user:
            user.last_login = timezone.now()  # last_login 갱신
            try:
                user.save(update_fields=['last_login'])
            except Exception as e:
                print(e)
                return Response(status=500)
            try:
                token = TokenObtainPairSerializer.get_token(user)
                refresh_token = str(token)
                access_token = str(token.access_token)
                return Response({'access_token': access_token, 'refresh_token': refresh_token})
            except Exception as e:
                print(e)
                return Response(status=500)
        else:
            return Response(status=400)