from django.db import models
from django.utils.translation import gettext as _

class Food(models.Model):
    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = 'غذا'
    FOOD_TYPE = [
        # ("breakfast","صبحانه"),
        ("drinks","نوشیدنی"),
        ("dinner","شام"),
        ("lunch","ناهار"),
    ]
    name = models.CharField(_("نام"),max_length=100)
    description = models.CharField(_("توضیحات"),max_length=500)
    rate = models.IntegerField(_("امتیاز"), default=0)
    price = models.IntegerField(_("قیمت"),)
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateField(_("زمان انتشار"),auto_now=False,auto_now_add=True)
    photo = models.ImageField(_("عکس"),upload_to = "foods/")
    type_food = models.CharField(_("نوع غذا"),max_length=10,choices=FOOD_TYPE,default="drinks")
    def __str__(self):
        return self.name


class HomePics(models.Model):
    homepic = models.ImageField(_("عکس های صفحه اصلی"),upload_to = "homepics/")
    picname = models.CharField(_("نام عکس"),max_length=100)

    def __str__(self):
        return self.picname

class SliderPics(models.Model):
    sliderpic = models.ImageField(_("عکس های صفحه اصلی"),upload_to = "sliderpics/")
    slidername = models.CharField(_("نام عکس"),max_length=100)

    def __str__(self):
        return self.slidername
