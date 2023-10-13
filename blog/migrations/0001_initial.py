# Generated by Django 4.1.4 on 2022-12-28 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان لاتین')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان لاتین')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('content', models.TextField(verbose_name='متن')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('image', models.ImageField(null=True, upload_to='blogs/', verbose_name='تصویر')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.category', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='blogs', to='blog.tag', verbose_name='تگ ها')),
            ],
            options={
                'verbose_name': 'بلاگ',
                'verbose_name_plural': 'بلاگ',
            },
        ),
    ]
