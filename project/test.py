from requesthandler import requesthandler
from dataparser import dataParser

class scraperPrototype(object):
	req = requesthandler()
	dp = dataParser()
	domain = ""
	parsed_urls = []
	def __init__(self, target=""):
		self.domain = target
	def parse_links(self):
		self.req.get(self.domain)
		self.dp.parse_links(self.req.data(), domain=self.domain)
		self.parsed_urls = self.dp.urls
