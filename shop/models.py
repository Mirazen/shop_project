from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [
        ('guest', 'Гость'),
        ('client', 'Клиент'),
        ('manager', 'Менеджер'),
        ('admin', 'Администратор'),
    ]
    role = models.CharField(max_length=20, choices=ROLES, default='client')
    third_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.third_name}"
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Supplier(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    UNITS = [
        ('шт', 'Штуки'),
        ('кг', 'Килограммы'),
        ('л', 'Литры'),
    ]

    name = models.CharField(max_length=300)
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    discount = models.IntegerField(default=0)
    unit = models.CharField(
        max_length=10,
        choices=UNITS,
        default='шт'
    )
    stock_quantity = models.IntegerField(
        default=0
    )
    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True,
    )

    def get_discount_price(self):
        if self.discount > 0:
            discount_amount = self.price * self.discount / 100
            return self.price - discount_amount
        return self.price
    
    def has_discount(self):
        return self.discount > 0

    def has_large_discount(self):
        return self.discount > 15

    def is_stock_empty(self):
        return self.stock_quantity == 0

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'