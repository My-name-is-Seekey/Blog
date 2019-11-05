from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序列号')
    name = models.CharField(max_length=32, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.CharField(max_length=4, verbose_name='性别')

    def __str__(self):
        name = "(" + str(self.id) + ')' + self.name
        return name

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
