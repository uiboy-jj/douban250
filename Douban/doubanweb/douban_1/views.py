import json
from django.db.models import Avg
from django.shortcuts import render
from .models import movie_data
from django.db.models import Avg,Max

from collections import Counter
# Create your views here.
# 主页函数
def index(request):

    comments_num_avg= movie_data.objects.all().aggregate(Avg('comments_num'))
    comments_num_max = movie_data.objects.all().aggregate(Max('comments_num'))
    score_avg = movie_data.objects.all().aggregate(Avg('score'))
    score_max = movie_data.objects.all().aggregate(Max('score'))
    avg_num = comments_num_avg['comments_num__avg']
    max_num = comments_num_max['comments_num__max']
    bv = ('%.1f' % score_avg['score__avg'])
    score_avg_num = bv
    score_max_num = score_max['score__max']

    a = list(movie_data.objects.values_list('type_one', flat=True))
    b = list(movie_data.objects.values_list('type_two', flat=True))
    c = list(movie_data.objects.values_list('type_three', flat=True))
    d = list(movie_data.objects.values_list('type_four', flat=True))
    e = list(movie_data.objects.values_list('type_five', flat=True))
    A = a+b+c+d+e
    B = dict(Counter(A))
    B.pop('无')

    max_value = max(B.values())
    for keys, values in B.items():
        if values == max_value:
            max_key = keys

    min_value = min(B.values())
    for keys, values in B.items():
        if values == min_value:
            min_key = keys

    directors = list(movie_data.objects.values_list('director', flat=True))
    directors_num_dict = dict(Counter(directors))
    director_max_value = max(directors_num_dict.values())
    for keys, values in directors_num_dict.items():
        if values == director_max_value:
            director_max_key = keys

    order_10 = list(movie_data.objects.filter(order__in=[1,2,3,4,5,6,7,8,9,10]).values_list('name', flat=True))
    order_102 = list(movie_data.objects.filter(order__in=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).values_list('comments_num', flat=True))
    name_10 = []
    for a in order_10:
       A = a.split()[0]

       name_10.append(A)
    numbers = [int(x) for x in order_102]
    print(name_10)
    print(numbers)
    # content = {}
    # content['B'] =json.dumps(numbers)
    # content['B1'] =json.dumps(name_10)
    # numbers = json.dumps(list(numbers))  # 封装数据 编码
    # numbers = json.loads(numbers)  # 解码
    # name_10 = json.dumps(list(name_10))  # 封装数据 编码
    # name_10 = json.loads(name_10)  # 解码

    # B = numbers
    # B1 = name_10
   # order_10 = list(movie_data.objects.values_list('order', flat=True))
    content_250 =movie_data.objects.values_list('name','order','score','comments_num')
    # name_250 = list(movie_data.objects.values_list('name', flat=True))
    # name_250_2 =[]
    # for a in name_250:
    #    A = a.split()[0]
    #
    #    name_250_2.append(A)
    #filter(order__in=[i for i in range(1,251)])
    content_250_2 = []
    for i in list(content_250):
        a = list(i)
        content_250_2.append(a)
    for i in content_250_2:
     i[0] = i[0].split()[0]




    return render(request, "index.html",locals())