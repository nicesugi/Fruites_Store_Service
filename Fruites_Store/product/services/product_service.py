from typing import Dict
from product.models import Product
from product.serializers import ProductSerializer


def get_product(page: int) -> ProductSerializer:
    """
    모든 상품의 조회를 담당하는 Service
    Args :
        page (int): 50개씩 상품 표시, url에 담아서 보내줌
    Return :
        get_product_serializer
    """
    get_products = Product.objects.all()
    first_index = page * 50
    end_index = first_index + 50
    
    if len(get_products) < first_index or page < 0:
        return []
    get_products_serializer = ProductSerializer(get_products[first_index:end_index], many=True)
    return get_products_serializer.data


def create_product(create_product_data: Dict[str, str]) -> None:
    """
    상품 생성을 담당하는 Service
    Args :
        create_product_data (dict) : {
            name (str): 상품의 제목,
            desc (str) : 상품의 내용
        }
    Return :
        None
    """
    product_serializer = ProductSerializer(data=create_product_data)
    product_serializer.is_valid(raise_exception=True)
    product_serializer.save()
    
    
def update_product(product_id: int, update_product_data: Dict[str, str]) -> Dict[str, str]:
    """
    상품 수정을 담당하는 Service
    Args :
        product_id (int): products.product 외래키, url에 담아서 보내줌,
        update_product_data (dict): {
            name (str): 상품의 제목 or
            desc (str): 상품의 내용
        }
    Return :
        dict[str, str]
    """
    update_product = Product.objects.get(id=product_id)
    update_product_serializer = ProductSerializer(update_product, update_product_data, partial=True)
    update_product_serializer.is_valid(raise_exception=True)
    update_product_serializer.save()
    return ({'update_product': update_product_serializer.data})


def delete_product(product_id: int) -> None:
    """
    상품 삭제를 담당하는 Service
    Args :
        product_id (int): products.product 외래키, url에 담아서 보내줌
    Return :
        None
    """
    delete_product = Product.objects.get(id=product_id)
    delete_product.delete()


def get_product_detail(product_id: int) -> ProductSerializer:
    """
    하나의 상품 상세정보 조회를 담당하는 Service
    Args :
        product_id (int): products.product 외래키, url에 담아서 보내줌
    Return :
        get_product_detail_serializer
    """
    product = Product.objects.get(id=product_id)
    get_product_detail_serializer = ProductSerializer(product)
    return get_product_detail_serializer.data
    