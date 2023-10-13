# Generated by Django 4.1.4 on 2022-12-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('rate', models.IntegerField(default=0, verbose_name='امتیاز')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('time', models.IntegerField(verbose_name='زمان لازم')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='زمان انتشار')),
                ('photo', models.ImageField(upload_to='foods/', verbose_name='عکس')),
                ('type_food', models.CharField(choices=[('drinks', 'نوشیدنی'), ('dinner', 'شام'), ('lunch', 'ناهار')], default='drinks', max_length=10, verbose_name='نوع غذا')),
            ],
            options={
                'verbose_name': 'غذا',
                'verbose_name_plural': 'غذا',
            },
        ),
        migrations.CreateModel(
            name='HomePics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepic', models.ImageField(upload_to='homepics/', verbose_name='عکس های صفحه اصلی')),
                ('picname', models.CharField(max_length=100, verbose_name='نام عکس')),
            ],
        ),
        migrations.CreateModel(
            name='SliderPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sliderpic', models.ImageField(upload_to='sliderpics/', verbose_name='عکس های صفحه اصلی')),
                ('slidername', models.CharField(max_length=100, verbose_name='نام عکس')),
            ],
        ),
    ]
