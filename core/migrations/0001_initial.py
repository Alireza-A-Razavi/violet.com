# Generated by Django 2.2 on 2020-09-09 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=164, unique=True)),
                ('featured', models.BooleanField(default=False)),
                ('on_discount', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=132, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('active', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
                ('discoutn_price', models.FloatField(blank=True, null=True)),
                ('on_discount', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=164)),
                ('featured', models.BooleanField(default=False)),
                ('on_discount', models.BooleanField(default=False)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='core.OrderItem')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producer', to='users.ProducerProfile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MainCategory'),
        ),
    ]
