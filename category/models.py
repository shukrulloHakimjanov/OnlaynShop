from django.db import models
from django.urls import reverse

class Category(models.Model):
    slug = models.SlugField(unique=True)
    category_name = models.CharField(max_length=100)
    description  = models.TextField(blank=True)
    cat_img = models.ImageField(upload_to='media/',blank=True)

    class  Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'    

    def get_url(self):
        return reverse('product_by_category', args=(self.slug))


    def str(self):
        return self.category_name