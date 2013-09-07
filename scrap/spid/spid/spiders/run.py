from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from spid.items import Residence
import urlparse

class ResidenceSpider(BaseSpider):
	name = "residence"
	allowed_domains = ["wesleyan.edu"]
	start_urls = ["http://www.wesleyan.edu/reslife/ugrad_housing/woodframes.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/res_halls.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/communitybasedliving.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/programhousing.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/apartments.html",]

	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		
		for url in hxs.select("//a[contains(@href, '/housing/')]/@href").extract():
			yield Request(urlparse.urljoin(response.url, url.strip()), callback=self.parse)

		print response.url


