# Generated by Django 2.2.1 on 2019-11-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterField(
            model_name='author',
            name='gender',
            field=models.IntegerField(choices=[(0, '男'), (1, '女')], verbose_name='性别'),
        ),
    ]