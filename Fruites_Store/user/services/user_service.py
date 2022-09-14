from typing import Dict
from user.models import User, Order
from user.serializers import UserSerializer, OrderSerializer


def get_user(username: int):
    """ 
        사용자이름에 해당하는 유저 정보 반환 함수

    Args:
        username (str): 사용자이름 

    Returns:
        user_info (dict) : 유저 정보

    Raises:


    """

    user_obj = User.objects.get(username=username)

    user_info = UserSerializer(user_obj).data

    return user_info


def create_user(user_info: dict):
    """ 
        사용자정보로 회원가입하는 함수

    Args:
        user_info (dict): 회원가입할 유저 정보 


    Raises:


    """

    user_serializer = UserSerializer(data=user_info)
    user_serializer.is_valid(raise_exception=True)
    user_serializer.save()


def update_user(user_obj: User, update_info: dict):
    """
        회원 정보 수정 함수

    Args:
        user_obj (User): 수정할 유저 오브젝트
        update_info (dict): 수정 정보 

    Returns:
        result (bool) : 회원탈퇴(비활성화) 성공 여부

    Raises:

    """

    # 현재 비밀번호 일치 여부 확인 코드
    cur_password = update_info.pop("old_password", None)
    if not user_obj.check_password(cur_password):
        return False

    # 새로운 비밀번호 수정정보에 추가
    new_password = update_info.pop("new_password", None)
    if new_password:
        update_info["password"] = new_password

    user_serializer = UserSerializer(user_obj, data=update_info, partial=True)
    user_serializer.is_valid(raise_exception=True)
    user_serializer.save()

    return True


def delete_user(user_obj: User):
    """회원탈퇴 기능 함수    

    Args:
        user_obj (User): 탈퇴할 유저 오브젝트

    Returns:
        result (bool) : 회원탈퇴(비활성화) 성공 여부

    """

    user_obj.is_active = False
    user_obj.save()

    return not user_obj.is_active


def get_order(user_id: int) -> OrderSerializer:
    """
    모든 상품의 조회를 담당하는 Service
    Args :
        username (str): 사용자이름 
    Return :
        get_order_serializer
    """
    get_orders = Order.objects.filter(user=user_id)
    get_orders_serializer = OrderSerializer(get_orders, many=True)
    return get_orders_serializer.data


def create_order(user_id: int, create_order_data: Dict[str, str]) -> Dict[str, str]:
    """
    상품 수정을 담당하는 Service
    Args :
        product_id (int): products.product 외래키, url에 담아서 보내줌,
        create_order_data (dict): {
            product (str): 주문한 상품의 정보 or
            count (str): 상품의 수량
        }
    Return :
        dict[str, str]
    """
    create_order_data["user"] = user_id
    order_serializer = OrderSerializer(data=create_order_data)
    order_serializer.is_valid(raise_exception=True)
    order_serializer.save()
    return ({'create_order': order_serializer.data})
    
    
def update_order(order_id: int, update_order_data: Dict[str, str]) -> Dict[str, str]:
    """
    상품 수정을 담당하는 Service
    Args :
        order_id (int): orders.order 외래키, url에 담아서 보내줌,
        update_order_data (dict): {
            product (str): 주문한 상품의 정보 or
            count (str): 상품의 수량
        }
    Return :
        dict[str, str]
    """
    update_order = Order.objects.get(id=order_id)
    update_order_serializer = OrderSerializer(update_order, update_order_data, partial=True)
    update_order_serializer.is_valid(raise_exception=True)
    update_order_serializer.save()
    return ({'update_order': update_order_serializer.data})


def delete_order(order_id: int) -> None:
    """
    주문 취소를 담당하는 Service
    Args :
        order_id (int): orders.order 외래키, url에 담아서 보내줌
    Return :
        None
    """
    delete_order = Order.objects.get(id=order_id)
    delete_order.delete()