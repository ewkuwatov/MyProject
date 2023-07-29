from django.db import models
from django.urls import reverse

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()



# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)
#
#     class Meta:
#         ordering = ('name')
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:detail', args=[self.id, self.slug])

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('product', 'quantity')
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField('Имя',max_length=150, db_index=True)
    image = models.ImageField(upload_to='static/img/comments', blank=True)
    description = models.TextField('Описание',max_length=1000, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name

