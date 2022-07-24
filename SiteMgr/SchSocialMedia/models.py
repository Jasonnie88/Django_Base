from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    content = models.CharField(max_length=300, verbose_name="文章内容")
    pub_date = models.DateField(verbose_name='发布日期', null=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'articleinfo'  # 指明数据库表名
        verbose_name = '文章'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

class ArticleComments(models.Model):
    comment = models.CharField(max_length=200, null=True, verbose_name='文章评论')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')

    class Meta:
        db_table = 'articlecomments'
        verbose_name = '文章评论'

    def __str__(self):
        return self.article

