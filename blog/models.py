from django.db import models
from django.utils import timezone

class Category(models.Model):
  name = models.CharField('カテゴリ',max_length=255)
  created_at = models.DateTimeField('作成日', default=timezone.now)

  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField('タイトル',max_length=255)
  text = models.TextField('本文')
  created_at = models.DateTimeField('作成日', default=timezone.now)
  #カテゴリを削除したときそれに紐付いたpostは削除しない
  category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT,blank=True, null=True)
  def __str__(self):
    return self.title

class Comment(models.Model):
  name = models.CharField('お名前',max_length=30,default='名無し')
  text = models.TextField('本文')
  post = models.ForeignKey(Post, verbose_name='紐づく記事', on_delete=models.PROTECT)
  created_at = models.DateTimeField('作成日',default=timezone.now)

  def __str__(self):
    return self.text[:10]