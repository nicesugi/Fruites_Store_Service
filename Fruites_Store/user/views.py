from rest_framework import permissions, status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.jwt_claim_serializer import FruitesTokenObtainPairSerializer

from user.services.user_service import (
    get_user,
    create_user,
    update_user,
    delete_user,
)


class TokenObtainPairView(TokenObtainPairView):
    """
    Login을 구현하는 View
    내부에서 UserLog를 생성하는 함수 내장
    """
    serializer_class = FruitesTokenObtainPairSerializer


class UserView(APIView):
    """
    User의 CRUD를 담당하는 View
    """
    permission_classes = [permissions.AllowAny]

    # 유저 조회 기능
    def get(self, request, username):
        res = get_user(username)
        return Response({'username': username, 'res': res}, status=status.HTTP_200_OK)

    # 회원가입 기능
    def post(self, request):
        try:
            create_user(request.data)
            return Response({'detail': '회원가입 성공'}, status=status.HTTP_201_CREATED)
        except AssertionError:
            return Response({'detail': '회원가입에 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 회원정보 수정기능
    def put(self, request):
        user_obj = request.user

        try:
            if update_user(user_obj, request.data):
                return Response({'detail': '회원정보 수정 성공'}, status=status.HTTP_201_CREATED)
            return Response({'detail': '비밀번호를 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'detail': '회원정보 수정에 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    # 회원탈퇴 기능
    def delete(self, request, username):
        user_obj = request.user
        print(user_obj)
        if delete_user(user_obj):
            return Response({'detail': '회원 탈퇴 성공'}, status=status.HTTP_200_OK)
        return Response({'detail': '회원 탈퇴에 실패했습니다.'}, status=status.HTTP_400_BAD_REQUEST)



