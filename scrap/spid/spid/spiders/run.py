from scrapy.spider import BaseSpider
from scrapy.selecter import HtmlPathSelector
from craigslist_sample.items import Residence

class ResidenceSpider(BaseSpider):
	name = "residence"
	allowed_domains = ["wesleyan.edu"]
	start_urls = ["http://www.wesleyan.edu/reslife/ugrad_housing/res_halls.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/communitybasedliving.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/programhousing.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/apartments.html",
		"http://www.wesleyan.edu/reslife/ugrad_housing/woodframes.html"]

	def parse(self, response):
		

