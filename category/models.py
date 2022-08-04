from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=60,unique=True)
    slug = models.SlugField(max_length=120,unique=True)
    description = models.TextField(max_length=268,blank=True)
    cart_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category'

    def get_url(self):
        #it means category slug
        return reverse('products_by_category',args=[self.slug])

    def __str__(self) -> str:
        return self.category_name