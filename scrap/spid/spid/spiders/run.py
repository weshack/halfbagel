from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from spid.items import Residence
from scrap import scrap
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

		# location
		location = hxs.select("//*[@id='header']/h1/text()").extract()
		if len(location) > 0:
			print "\nlocation: " + location[0]

		# units
		units = hxs.select("//*[@id='col2']/h3/text()").extract()
		if len(units) > 0:
			if 'quiet' in units[0]:
				print "quiet: " + str(1)
			else: print "quiet: " + str(0)

		# common_area
		common_area = hxs.select("//*[@id='col2']/unit-description/ul[1]/li[contains(text(), 'Common')]/text()").extract()
		if len(common_area) > 0:
			print "common: " + common_area[0][13:]

		# kitchen
		kitchen = hxs.select("//*[@id='col2']/unit-description/ul[2]/li[contains(text(), 'Kitchen')]/text()").extract()
		if len(kitchen) > 0:
			print "kitchen: " + kitchen[0][9:]

		# bathrooms
		bathrooms = hxs.select("//*[@id='col2']/unit-description/ul[3]/li[contains(text(), 'Bathroom')]/text()").extract()
		if len(bathrooms) > 0:
			print "bathroom(s): " + bathrooms[0][13:]

		# bedrooms
		bedrooms = hxs.select("//*[@id='col2']/unit-description/ul[4]/li[contains(text(), 'Bedroom')]/text()").extract()
		if len(bedrooms) > 0:
			print "bedroom(s): " + bedrooms[0][10:]

		# description
		descriptions = hxs.select("//unit-description//li").extract()
		print "description:"
		for d in descriptions:
			print d

		# program
		if 'program' in response.url:
			print "program: " + str(1)
		else: print "program: " + str(0)

		# wood
		if 'wood' in response.url: 
			print "wood: " + str(1)
		else: print "wood: " + str(0)

		# image
		image = hxs.select("//div[@id='col1']/img/@src").extract()
		if len(image) > 0: 
			print "image: " + urlparse.urljoin(response.url, image[0])

		# floorplans
		floorplans = hxs.select("//*[@id='col2']/unit-description/p[7]/a/@href").extract()
		floorplans_list = []
		for f in floorplans:
			floorplans_list.append(urlparse.urljoin(response.url, f))
		print floorplans_list



