# Generated by Django 5.1.5 on 2025-02-03 06:32

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_data',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='available_copies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LMS_app.booktype'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='total_copies',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booktype',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='borrowingrecord',
            name='due_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2025, 3, 5, 12, 17, 51, 662568)),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(default='Unknown Address', max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default='0000000000', max_length=10),
        ),
    ]
