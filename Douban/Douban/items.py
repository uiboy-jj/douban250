# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    order = scrapy.Field()#排榜顺序
    name = scrapy.Field()#电影名称
    director = scrapy.Field()#导演
    screenwriter = scrapy.Field()#编剧
    #starring = scrapy.Field()#主演
    type = scrapy.Field()#电影类型
  #  place = scrapy.Field()#制片地
   # language = scrapy.Field()#语言
   # time = scrapy.Field()#上映时间
    score = scrapy.Field()#评分
    comments_num = scrapy.Field()#评价人数
   # whether_play = scrapy.Field()#能否播放
    #play_link = scrapy.Field()#播放链接


