from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from gplaycrawler_pj.items import GplaycrawlerItem
from urllib.parse import urlparse
import json

class MySpider(CrawlSpider):
  name = "playcrawler"
  allowed_domains = ["play.google.com"]
  start_urls = ["https://play.google.com/store/apps/"]
  rules = [Rule(LinkExtractor(allow=(r'apps',),deny=(r'reviewId')),follow=True,callback='parse_link')]
    	# r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
    	#Rule(LinkExtractor(allow=(r'apps')),follow=True,callback='parse_link')]
    	# r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs
  def abs_url(url, response):
      """Return absolute link"""
      base = response.xpath('/html/head/base/@href').extract()
      if base:
        base = base[0]
      else:
        base = response.url
      return urlparse.urljoin(base, url)
    
  def parse_link(self,response):
      hxs = Selector(response)
      items = []
      item = GplaycrawlerItem()
      item["Link"] = ''.join(hxs.xpath('/html/head/link[5]/@href').extract())
      item["Item_name"] = ''.join(hxs.xpath('/html/head/title/text()').extract())
      item["Updated"] = ''.join(hxs.xpath('//div[11]/text()').extract())
      items.append(item)
      print(item)

      return items

      

