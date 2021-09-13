from django.db import models

# Create your models here.
#comments_num,director,name,order,screenwriter,type_one,type_two,type_three,type_four,type_five,score
class movie_data(models.Model):


    comments_num = models.CharField(max_length=128,verbose_name='评论人数',blank=False)
    director = models.CharField(max_length=128, verbose_name='导演', blank=False)
    name = models.CharField(max_length=128, verbose_name='名称', blank=False)
    order = models.CharField(max_length=128, verbose_name='排名', blank=False)
    screenwriter = models.CharField(max_length=128, verbose_name='编剧', blank=False)
    type_one = models.CharField(max_length=128,verbose_name='类型1',blank=False)
    type_two = models.CharField(max_length=128, verbose_name='类型2', blank=False)
    type_three = models.CharField(max_length=128, verbose_name='类型3', blank=False)
    type_four = models.CharField(max_length=128, verbose_name='类型4', blank=False)
    type_five = models.CharField(max_length=128, verbose_name='类型5', blank=False)
    score = models.CharField(max_length=128, verbose_name='评分', blank=False)



    class Meta:
        verbose_name_plural = 'Top250' #设置这个模型在后台的名字
