# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import re
import datetime
from zhihu.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT

def get_num(text):
    pattern = re.match('.*?(\d+).*', text)
    if pattern:
        nums = int(pattern.group(1))
    else:
        nums = 0
    return nums



class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuestionItem(scrapy.Item):
    question_id = scrapy.Field() # 问题id
    title = scrapy.Field()       # 标题
    theme = scrapy.Field()       # 主题分类
    url = scrapy.Field()
    content = scrapy.Field()
    attention = scrapy.Field()   # 关注人数
    browse = scrapy.Field()      # 浏览人数
    creat_time = scrapy.Field()  # 创建时间
    crawl_time = scrapy.Field()  # 爬取时间
    answer_num = scrapy.Field()  # 回答人数
    comment_num = scrapy.Field() # 评论人数

    def get_insert_sql(self):
        # 将数据插入mysql
        insert_sql = '''
                insert into question(question_id, title, theme, url, content, attention,browse, 
                creat_time, crawl_time, answer_num, comment_num) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
        question_id = int(''.join(self['question_id']))
        theme = ','.join(self['theme'])
        title = ''.join(self['title'])
        content = ''.join(self['content'])
        url = self['url'][0]
        attention = int(self['attention'][0].replace(',', ''))
        browse = int(self['attention'][1].replace(',', ''))
        creat_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)
        answer_num = get_num(self['answer_num'][0])
        comment_num = get_num(self['comment_num'][1])
        params = (question_id, title, theme, url, content, attention,browse, \
                creat_time, crawl_time, answer_num, comment_num)
        return insert_sql, params


class AnswerItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    question_id = scrapy.Field()
    url = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    praise_num = scrapy.Field()
    comment_num = scrapy.Field()
    creat_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_insert_sql(self):
        # 将回答插入mysql
        insert_sql = '''
            insert into answer(zhihu_id, question_id, url, author_id, content, praise_num, comment_num, creat_time,
                update_time, crawl_time) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        creat_time = datetime.datetime.fromtimestamp(self['creat_time'])
        update_time = datetime.datetime.fromtimestamp(self['update_time'])
        params = (self['zhihu_id'], self['question_id'], self['url'], self['author_id'], self['content'], \
                  self['praise_num'], self['comment_num'], creat_time, update_time, \
                  self['crawl_time'].strftime(SQL_DATETIME_FORMAT))
        return insert_sql, params

