from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CommModel(models.Model):
    objects = models.Manager()

    class Meta:
        # 此类可以当做父类，被其他model继承。字段自动过度给，继承的model
        abstract = True  # 【django以后做数据库迁移时， 不再为CommModel类创建相关的表以及表结构了】


class Article(CommModel):

    name = models.CharField(max_length=20, verbose_name='名称')
    content = models.TextField(max_length=300, verbose_name='文章内容') #.CharField(max_length=300, verbose_name="文章内容")
    pub_date = models.DateField(verbose_name='发布日期', auto_now=True)
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'articleinfo'  # 指明数据库表名
        verbose_name = '文章'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class PeopleInfo(CommModel):
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
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleComments(CommModel):
    comment = models.CharField(max_length=200, null=True, verbose_name='文章评论')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章')  # 外键
    pub_date = models.DateField(verbose_name='发布日期', auto_now=True)

    class Meta:
        db_table = 'articlecomments'
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment[0:10]


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)
    #objects = models.Manager()

    class Meta:
        db_table = 'tb_users'
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name

