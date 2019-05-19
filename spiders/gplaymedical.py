from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from gplayscrapper.items import GplaycrawlerItem
import urlparse
import json

class MySpider(CrawlSpider):
  name = "gplaymedical"
  allowed_domains = ["play.google.com"]
  start_urls = ["https://play.google.com/store/apps/category/MEDICAL"]
  rules = (
        Rule(LinkExtractor(allow=('/store/apps/category/MEDICAL/collection/topselling_paid/',)),follow=True),
        Rule(LinkExtractor(allow=('/store/apps/details\?')),follow=True,callback='parse_link')
        )

  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('//head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)
    
  def parse_link(self,response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.xpath('/html')
      items = []
      for titles in titles :
        item = GplaycrawlerItem()
        item["Item_name"] = titles.xpath('//*[@class="AHFaub"]/span/text()').extract()
        item["Link"] = titles.xpath('head/link[5]/@href').extract()
        item["Price"] = titles.xpath('//*[@itemprop="price"]/@content').extract()
        item["Genre"] = titles.xpath('//*[@itemprop="genre"]/text()').extract()
        item["Rating_value"] = titles.xpath('//*[@class="BHMmbe"]/text()').extract()
        item["Description"] = titles.xpath('//*[@jsname="sngebd"]/text()').extract()
        genre=str(item["Genre"])
        genre=genre[3:-2]
        print(genre)
        if(genre!='Medical'):
            continue
        items.append(item)
        print(item["Link"])
      return items
      

