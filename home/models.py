from django.db import models
from django.shortcuts import redirect
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=30)
    slug = models.SlugField(blank=True,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Slider(models.Model):
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to="media")
    url = models.URLField(max_length=100,default=False)

    def __str__(self):
        return self.description


class Ads(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media")
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to="media")
    slug = models.SlugField(blank=True,unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

LABELS=(('hot','Hot'),('new','New'),('sale','Sale'))

STOCK = (('in stock','In stock'), ('out of stock','Out of stock'))

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to="media")
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    stock = models.CharField(max_length=100,choices=STOCK)
    labels = models.CharField(max_length=100,choices=LABELS)
    description = models.TextField(blank=True)
    scpecification = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    post = models.CharField(max_length=300)
    feedback = models.TextField()

    def __str__(self):
        return self.name

class ProductReviews(models.Model):
    slug = models.SlugField(blank=True,unique=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    review = models.TextField(blank=True)
    stars = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Cart(models.Model):
    username = models.CharField(max_length=100)
    slug = models.SlugField(blank=True,unique=False)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=0)
    checkout = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


