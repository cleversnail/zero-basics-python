from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="文章标题")
    pub_date = models.DateTimeField(verbose_name="发布日期")
    data = models.TextField(max_length=200, verbose_name="文章内容")

