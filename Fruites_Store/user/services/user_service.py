from user.models import User
from user.serializers import UserSerializer


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