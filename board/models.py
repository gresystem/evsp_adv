from django.db import models
from evuser.models import Evuser
from tag.models import Tag

# Create your models here.

class Board(models.Model):
  title = models.CharField(max_length=128, verbose_name='제목')
  user = models.ForeignKey('evuser.Evuser', on_delete=models.CASCADE, verbose_name='작성자')
  content = models.TextField(verbose_name='내용')
  image = models.ImageField(blank=True, null=True)
  # tags = models.ManyToManyField('tag.Tag', verbose_name='테그')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'evsp_board'
    verbose_name = '게시글'
    verbose_name_plural = '게시글'


# https://startbootstrap.com/themes/clean-blog/ 참조하여 UI 구성해 보면 좋을 듯
