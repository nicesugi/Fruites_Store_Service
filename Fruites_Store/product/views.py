from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from product.services.product_service import (
    get_product,
    create_product,
    update_product,
    delete_product,
    get_product_detail
)
from product.models import Product


class ProductView(APIView):
    """
    상품의 CRUD를 담당하는 View
    """
    def get(self, request):
        params = request.GET.get('page', '1')
        page = int(params) - 1
        products_serializer = get_product(page)
        return Response(products_serializer, status=status.HTTP_200_OK)


    def post(self, request):
        try:
            if request.data:
                create_product(request.data)
                return Response({'detail': '상품을 등록했습니다.'}, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError as e:
            name = list(e.detail.keys())[0]
            error = ''.join([str(value) for values in e.detail.values() for value in values])
            return Response({name: error}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            if request.data['desc'] == {}:
                return Response({'detail': '수정할 내용이 비어있습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            if product.desc == request.data['desc']: 
                return Response({'detail': '수정할 내용을 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST) 
            updated_log = update_product(product_id, request.data)
            return Response(updated_log, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({'detail': '수정할 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)    
            delete_product(product_id)
            return Response({'detail': '상품이 삭제되었습니다.'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'detail': '삭제할 상품이 존재하지 않습니다.'}, status=status.HTTP_404_NOT_FOUND)
        
        
class ProductDetailView(APIView):
    """
    상품 상세 정보 담당하는 View
    """
    def get(self, request, product_id):
        products_serializer = get_product_detail(product_id)
        return Response(products_serializer, status=status.HTTP_200_OK)