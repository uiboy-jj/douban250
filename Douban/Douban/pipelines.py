# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import CsvItemExporter

class DoubanFilePipeline(object):
        def open_spider(self, spider):  # 在爬虫开启的时候仅执行一次
          if spider.name == 'movie':

                self.file = open("movie.csv", "ab+")
                self.exporter = CsvItemExporter(self.file, encoding='utf-8-sig')
                self.exporter.start_exporting()


        def close_spider(self, spider):  # 在爬虫关闭的时候仅执行一次
          if spider.name == 'movie':
                self.exporter.finish_exporting()
                self.file.close()

        def process_item(self, item, spider):
            if spider.name == 'movie':
                self.exporter.export_item(item)

            # 不return的情况下，另一个权重较低的pipeline将不会获得item
            return item
