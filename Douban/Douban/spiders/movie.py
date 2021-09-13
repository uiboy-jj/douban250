# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem
from lxml import etree
class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = [
                 #'https://movie.douban.com/top250'
                  'https://movie.douban.com/top250?start=25&filter='
                  #'https://movie.douban.com/top250?start=50&filter='
                  #'https://movie.douban.com/top250?start=75&filter='
                  #'https://movie.douban.com/top250?start=100&filter='
                  #'https://movie.douban.com/top250?start=125&filter='
                  #'https://movie.douban.com/top250?start=150&filter='
                  #'https://movie.douban.com/top250?start=175&filter='
                  #'https://movie.douban.com/top250?start=200&filter='
                   #'https://movie.douban.com/top250?start=225&filter='
                    ]

    def start_requests(self):  # 重构start_requests方法
        # 这个cookies_str是抓包获取的
        #cookies_str = 'bid=dn-cU54k5kc; ap_v=0,6.0; push_doumail_num=0; push_noty_num=0; __utma=30149280.782481749.1630297594.1630297594.1630297594.1; __utmc=30149280; __utmz=30149280.1630297594.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=30149280.22573; __utmc=223695111; dbcl2="225736133:Dy32zxXNP4c"; ck=jLkr; __utmt=1; __utmb=30149280.8.10.1630297594; ll="118281"; __utma=223695111.1569998650.1630298013.1630298013.1630300806.2; __utmb=223695111.0.10.1630300806; __utmz=223695111.1630300806.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ses.100001.4cf6=*; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1630300806%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=DAE529127AFAF5EA345E61DC10B55126D|1d8825cb905cafb4161037dff964eb2f; __gads=ID=a60a38c0f590ea34-221af3473ccb00f5:T=1630297593:RT=1630300910:S=ALNI_MY7Yn8i9Nbijaj8cm8F11qx8b9ang; _pk_id.100001.4cf6=323e8f4020f4ba8e.1630298013.2.1630300919.1630298976.'  # 抓包获取
        # 将cookies_str转换为cookies_dict
        cookies_str = 'bid=dn-cU54k5kc; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmz=30149280.1630297594.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=30149280.22573; __utmc=223695111; dbcl2="225736133:Dy32zxXNP4c"; ck=jLkr; ll="118281"; __utmz=223695111.1630300806.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=DAE529127AFAF5EA345E61DC10B55126D|1d8825cb905cafb4161037dff964eb2f; __gads=ID=a60a38c0f590ea34-221af3473ccb00f5:T=1630297593:RT=1630300910:S=ALNI_MY7Yn8i9Nbijaj8cm8F11qx8b9ang; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1630418084%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.782481749.1630297594.1630297594.1630418084.2; __utmb=30149280.0.10.1630418084; __utma=223695111.1569998650.1630298013.1630300806.1630418084.3; __utmb=223695111.0.10.1630418084; ap_v=0,6.0; _pk_id.100001.4cf6=323e8f4020f4ba8e.1630298013.3.1630418435.1630302962.'
        cookies_dict = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict
        )


    def parse(self, response):
        item = DoubanItem()
        #提前详情页面url
        movie_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/@href').extract()
        #palce = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[2]')
        #item['place'] = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[1]/text()[2]').extract()
        # for movie,pla in zip(movie_list,palce):
        #     url = movie
        #     places =str(pla).replace(' ','').split('/')[1]
        #     yield scrapy.Request(url = url, callback=self.detail_parse,meta={"palce":places})
        for movie in movie_list:
            url = movie
            yield scrapy.Request(url = url, callback=self.detail_parse)

        # '''//*[@id="content"]/div/div[1]/div[2]/span[3]/a'''
        # next_url = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        # if next_url != None:
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(url=next_url,callback = self.parse)


    def detail_parse(self,response):
        ''' order = scrapy.Field()#排榜顺序
            name = scrapy.Field()#电影名称
            director = scrapy.Field()#导演
            screenwriter = scrapy.Field()#编剧
            starring = scrapy.Field()#主演
            type = scrapy.Field()#电影类型
            place = scrapy.Field()#制片地
            language = scrapy.Field()#语言
            time = scrapy.Field()#上映时间
            score = scrapy.Field()#评分
            comments_num = scrapy.Field()#评价人数
            whether_play = scrapy.Field()#能否播放
            play_link = scrapy.Field()#播放链接

            '''
        item = DoubanItem()
       # item['name'] = response.xpath('//*[@id="content"]/h1/a/text()').extract_first()
        item['order'] = response.xpath('//*[@id="content"]/div[1]/span[1]/text()').extract_first()
        item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['screenwriter'] = response.xpath('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
        #item['starring'] = response.xpath('//*[@id="info"]/span[3]/span[2]/span/a/text()').extract()
        item['type'] = response.xpath('//*[@id="info"]/span[@property="v:genre"]/text()').extract()
       # item['place'] = response.meta['palce']
       # item['time'] = response.xpath('//*[@id="content"]/h1/span/text()').extract_first()
        item['name'] = response.xpath('//*[@id="content"]/h1/span/text()').extract_first()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()
        item['comments_num'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract_first()
        #item['play_link'] = response.xpath('//*[@id="content"]/h1/a/@href').extract_first()

        yield item

