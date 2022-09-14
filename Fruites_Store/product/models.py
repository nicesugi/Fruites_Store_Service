from django.db import models


class Product(models.Model):
    STATUS_CHOICES = (
    ('sale', '판매중'),
    ('sold_out', '품절'),
    )
    
    name = models.CharField('이름', max_length=200)
    desc = models.TextField('설명')
    price = models.PositiveIntegerField('금액', default=0)
    delivery_fee = models.PositiveIntegerField('배송비', default=0)
    count = models.PositiveIntegerField('재고', default=0)
    status = models.CharField('판매상태', max_length=10, choices=STATUS_CHOICES, default='sale')
    
    def __str__(self):
        return self.name