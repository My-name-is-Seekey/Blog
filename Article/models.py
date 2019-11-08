from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=32, verbose_name='类型')
    descriptions = models.TextField(verbose_name='描述')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'
        verbose_name = '类型'
        verbose_name_plural = verbose_name


class Author(models.Model):
    GENDER_LIST = [(0, '男'), (1, '女')]
    name = models.CharField(max_length=32, verbose_name='姓名')
    gender = models.IntegerField(choices=GENDER_LIST, verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class Article(models.Model):
    LIST = [(0, '不推荐'), (1, '推荐')]
    title = models.CharField(max_length=32, verbose_name='标题')
    date = models.DateField(auto_now=True, verbose_name='日期')
    # content = models.TextField(verbose_name='文章内容')
    content = RichTextField(verbose_name='文章内容')
    # description = models.TextField(verbose_name='描述')
    description = RichTextField(verbose_name='描述')
    recommend = models.IntegerField(verbose_name='推荐', choices=LIST, default=0)
    click = models.IntegerField(verbose_name='点击率')
    picture = models.ImageField(upload_to='images', default='images/02.jpg', verbose_name='图片')
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
