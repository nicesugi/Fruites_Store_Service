# Generated by Django 4.1.1 on 2022-09-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='이름')),
                ('desc', models.TextField(verbose_name='설명')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='금액')),
                ('delivery_fee', models.PositiveIntegerField(default=0, verbose_name='배송비')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='재고')),
                ('status', models.CharField(choices=[('sale', '판매중'), ('sold_out', '품절')], default='sale', max_length=10, verbose_name='판매상태')),
            ],
        ),
    ]