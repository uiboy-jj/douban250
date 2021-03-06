# Generated by Django 3.2 on 2021-09-09 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_num', models.CharField(max_length=128, verbose_name='评论人数')),
                ('director', models.CharField(max_length=128, verbose_name='导演')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('order', models.CharField(max_length=128, verbose_name='排名')),
                ('screenwriter', models.CharField(max_length=128, verbose_name='编剧')),
                ('type_one', models.CharField(max_length=128, verbose_name='类型1')),
                ('type_two', models.CharField(max_length=128, verbose_name='类型2')),
                ('type_three', models.CharField(max_length=128, verbose_name='类型3')),
                ('type_four', models.CharField(max_length=128, verbose_name='类型4')),
                ('type_five', models.CharField(max_length=128, verbose_name='类型5')),
                ('score', models.CharField(max_length=128, verbose_name='评分')),
            ],
            options={
                'verbose_name_plural': 'Top250',
            },
        ),
    ]
