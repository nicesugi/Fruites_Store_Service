from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('사용자 계정을 만들어주세요')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    USER_CHOICES = (
    ('manager', '관리자'),
    ('general', '사용자'),
    )
    username = models.CharField('사용자 이름', max_length=30, unique=True)
    password = models.CharField('비밀번호', max_length=128)
    address = models.CharField('배송지', max_length=20, blank=True)
    type = models.CharField('사용자 유형', max_length=10, choices=USER_CHOICES, default='general', blank=True)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label): 
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    
class OrderStatus(models.Model):
    ORDER_CHOICES = (
    ('waiting_for_payment', '결제대기'),
    ('complete_payment', '결제완료 & 주문대기'),
    ('order_completed', '주문완료'),
    ('order_cancel', '주문취소'),
    ('waiting_for_delivery', '배송대기'),
    ('shipping', '배송중'),
    ('delivery_completed', '배송완료'),
    )
    status = models.CharField('주문상태', max_length=20, choices=ORDER_CHOICES, default='waiting_for_payment')
    
    def __str__(self):
        return self.status
    

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name='주문자', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name='주문상품', on_delete=models.SET_NULL, null=True)
    order_status = models.ForeignKey(OrderStatus, verbose_name='주문상태', on_delete=models.SET_NULL, null=True, blank=True)
    count = models.PositiveIntegerField('수량', default=0)
    created_at = models.DateTimeField('주문날짜', auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} 님의 주문 : {self.product}'