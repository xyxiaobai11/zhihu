# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin
import re
from scrapy.loader import ItemLoader
from zhihu.items import QuestionItem, AnswerItem
import datetime
import json

class QuestionSpider(scrapy.Spider):
    name = 'question'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_answer_url = 'https://www.zhihu.com/api/v4/questions/{0}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset={1}&limit={2}&sort_by=default&platform=desktop'

    def parse(self, response):
        # with open('./zhihu.html', 'w', encoding='utf8') as f:
        #     f.write(response.text)
        all_urls = response.css('a::attr(href)').extract()
        all_urls = [urljoin(response.url, url) for url in all_urls]
        all_urls = [url for url in all_urls if url.startswith('https')]
        for url in all_urls:
            pattern = re.match('(.*zhihu.com/question\/(\d+))(/|$).*', url)
            if pattern:
                request_url = pattern.group(1)
                question_id = pattern.group(2)
                yield scrapy.Request(request_url, meta={'question_id': question_id}, callback=self.parse_question)
            else:
                # 不满足问题页面 继续请求跟踪
                yield scrapy.Request(url, callback=self.parse)

    def parse_question(self, response):
        loader = ItemLoader(item=QuestionItem(), response=response)
        loader.add_xpath('title', "//div[@class='QuestionHeader-main']/h1/text()")
        content = response.xpath("//div[@class='QuestionHeader-detail']//span//text()").extract_first(' ')
        loader.add_value('content', content)
        loader.add_value('url', response.url)
        loader.add_value('question_id', response.meta.get('question_id'))
        # 浏览人数 和 关注人数
        loader.add_xpath('attention', "//div[@class='QuestionFollowStatus']//strong[@class='NumberBoard-itemValue']/text()")
        loader.add_xpath('comment_num', "//div[@class='QuestionHeader-Comment']//text()")
        loader.add_xpath('answer_num', "//h4[@class='List-headerText']//text()")
        loader.add_xpath('theme', "//div[@class='QuestionHeader-topics']//div[@class='Popover']//text()")
        #loader.add_value('crawl_time', datetime.datetime.now())
        loader.add_css('answer_num', '.List-headerText')

        question_item = loader.load_item()

        yield scrapy.Request(self.start_answer_url.format(response.meta.get('question_id', ''), 0, 20),callback=self.parse_answer)
        yield question_item

    def parse_answer(self, response):
        #print(response.text)
        json_data = json.loads(response.text)
        is_end = json_data['paging']['is_end']
        next_url = json_data['paging']['next']

        for answer in json_data['data']:
            answer_item = AnswerItem()
            answer_item['zhihu_id'] = answer['id']
            answer_item['question_id'] = answer['question']['id']
            answer_item['url'] = response.url
            answer_item['author_id'] = answer['author']['id'] if 'id' in answer['author'] else ' '
            answer_item['content'] = answer['content'] if 'content' in answer else ' '
            answer_item['praise_num'] = answer['voteup_count']
            answer_item['comment_num'] = answer['comment_count']
            answer_item['creat_time'] = answer['created_time']
            answer_item['update_time'] = answer['updated_time']
            answer_item['crawl_time'] = datetime.datetime.now()

            yield answer_item

        if is_end == 'false':
            yield scrapy.Request(next_url, callback=self.parse_answer)
