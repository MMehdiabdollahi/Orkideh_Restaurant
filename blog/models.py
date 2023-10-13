from distutils.command.upload import upload
from email.mime import image
import imp
from importlib.resources import contents
from tabnanny import verbose
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.forms import ImageField
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

# Create your models here.

class Blog(models.Model):
    class Meta:
        verbose_name= "بلاگ"
        verbose_name_plural = 'بلاگ'
    title = models.CharField(_("عنوان"),max_length=50)
    description = models.CharField(_("توضیحات"),max_length=100)
    content = models.TextField(_("متن"))
    created_at = models.DateTimeField(_("زمان انتشار"),default=timezone.now)
    author = models.ForeignKey(User,verbose_name=_("نویسنده"),on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"),upload_to="blogs/",null = True)
    tags = models.ManyToManyField("Tag",verbose_name=_("تگ ها"),related_name="blogs",blank=True,null=True) 
    category = models.ForeignKey("Category",related_name="blog",verbose_name=_("دسته بندی"), on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    class Meta:
        verbose_name= "دسته بندی"
        verbose_name_plural = 'دسته بندی'

    title = models.CharField(_("عنوان"),max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    class Meta:
        verbose_name= "تگ"
        verbose_name_plural = 'تگ'
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    update_at = models.DateTimeField(_("تاریخ بروز رسانی"),auto_now=True,auto_now_add=False)
    def __str__(self):
        return self.title