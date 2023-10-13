from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Contact(models.Model):
    class Meta:
        verbose_name = 'پیام های کاربران'
        verbose_name_plural = 'پیام های کاربران'
    
    username = models.CharField(_("نام و نام خانوادگی"),max_length=200)
    useremail = models.EmailField(_("ایمیل"),max_length=254)
    usertext = models.TextField(_("متن"))
    
    def __str__(self):
        return self.username