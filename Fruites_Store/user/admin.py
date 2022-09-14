from django.contrib import admin
from user.models import (
    User,
    OrderStatus,
    Order,
)


admin.site.register(User)
admin.site.register(OrderStatus)
admin.site.register(Order)