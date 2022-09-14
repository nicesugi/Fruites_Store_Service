from rest_framework import permissions, status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# from Fruites_Store.user.serializers import OrderSerializer
from user.jwt_claim_serializer import FruitesTokenObtainPairSerializer

from user.models import User
from user.services.user_service import (
    get_user,
    create_user,
    update_user,
    delete_user,
)
from user.services.user_service import (
    get_order,
    create_order,
    update_order,
    delete_order,
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



class OrderView(APIView):
    """
    상품 주문의 CRUD를 담당하는 View
    """
    def get(self, request, user_id):
        orders_serializer = get_order(user_id)
        return Response(orders_serializer, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': '로그인이 필요합니다.'}, status=status.HTTP_404_NOT_FOUND)
        if request.data:
            create_order(user_id, request.data)
            return Response({'detail': '상품이 주문 완료 되었습니다.'}, status=status.HTTP_201_CREATED)

    def put(self, request, order_id):
        try:
            user = request.user
            if request.data['count'] == {}:
                return Response({'detail': '수량이 비어있습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            updated_log = update_order(order_id, request.data)
            return Response(updated_log, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'detail': '로그인이 필요합니다.'}, status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request, order_id):
        try:
            user = request.user
            delete_order(order_id)
            return Response({'detail': '주문이 취소되었습니다.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'detail': '로그인이 필요합니다.'}, status=status.HTTP_404_NOT_FOUND)
        
