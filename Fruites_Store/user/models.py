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