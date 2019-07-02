# Generated by Django 2.1 on 2019-05-23 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190523_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default='なし', on_delete=django.db.models.deletion.PROTECT, to='blog.Category', verbose_name='カテゴリ'),
        ),
    ]