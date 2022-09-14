# Generated by Django 4.1.1 on 2022-09-14 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('waiting_for_payment', '결제대기'), ('complete_payment', '결제완료 & 주문대기'), ('order_completed', '주문완료'), ('order_cancel', '주문취소'), ('waiting_for_delivery', '배송대기'), ('shipping', '배송중'), ('delivery_completed', '배송완료')], default='waiting_for_payment', max_length=20, verbose_name='주문상태')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='수량')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='주문날짜')),
                ('order_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.orderstatus', verbose_name='주문상태')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='주문상품')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='주문자')),
            ],
        ),
    ]