import re
from urlqueue import UrlQueue

'''
The Data Parser class has no special constructor, but has methods to handle raw site data that was downloaded from the requests class. This class is intended to find all instances of the href tags within a page and will populate the 
'''

class dataParser(object):
	raw_data = ""
	anchor_href_expression = "href=\"([a-zA-Z.?:/&=@]*)\"" #This is a regular expression. Don't panic.
	urls = []
	url_queue = UrlQueue()
	def parse_links(self, raw_data, domain=""):
		anchor_list = re.findall(self.anchor_href_expression, str(raw_data))
		for x in range(len(anchor_list)):
			if anchor_list[x][0] == '/' and anchor_list[x] not in self.urls:
				self.urls.append(domain + anchor_list[x])
			elif anchor_list[x] not in self.urls:
				self.urls.append(anchor_list[x])
		return self.urls
	def queue_links(self):
		for x in self.urls:
			self.url_queue.add_to_spider(self.urls[x])
