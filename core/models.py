from django.db import models
from django.shortcuts import reverse, redirect
from django.utils.text import slugify
from users.models import ProducerProfile, User

class MainCategory(models.Model):
    title = models.CharField(max_length=164)
    featured = models.BooleanField(default=False)
    on_discount = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:main-categories", kwargs={
            'slug': self.slug
        })



class Category(models.Model):
    title = models.CharField(max_length=164, unique=True)
    sub_category_of = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    on_discount = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:categories", kwargs={
            'slug': self.slug
        })


class Item(models.Model):
    title = models.CharField(max_length=132, unique=True)
    image = models.ImageField()
    price = models.FloatField()
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True)
    discoutn_price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    on_discount = models.BooleanField(default=False)    


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.item.title





class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producer = models.ForeignKey(ProducerProfile, on_delete=models.CASCADE,  related_name='producer')
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



#create database for addresses, refunds and main,


class ContactTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()

    def __str__(self):
        return self.first_name

class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


