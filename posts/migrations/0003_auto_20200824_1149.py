# Generated by Django 3.1 on 2020-08-24 02:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200819_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='p_idx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.park_number'),
        ),
        migrations.AlterField(
            model_name='post',
            name='starpoint',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='별점1~5'),
        ),
    ]
