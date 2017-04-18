import re
from urlqueue import UrlQueue

'''
The Data Parser class has no special constructor, but has methods to handle raw site data that was downloaded from the requests class. This class is intended to find all instances of the href tags within a page and will populate the 
'''

class dataParser(object):
	raw_data = ""
	anchor_href_expression = "href=\"([a-zA-Z.?:/&=@]*)\"" #This is a regular expression. Don't panic.
	email_link_expression = "([a-zA-Z1-9.\-]*\@[a-zA-Z1-9.\-]*\.[a-zA-Z1-9.\-]*)" #This is the regex for an email link. It may also pick up weird malformed ones as well.
	urls = []
	email_links = []
	def parse_links(self, raw_data, domain=""):
		anchor_list = re.findall(self.anchor_href_expression, str(raw_data))
		for x in range(len(anchor_list)):
			if anchor_list[x][0] == '/' and anchor_list[x] not in self.urls:
				self.urls.append(domain + anchor_list[x])
			elif anchor_list[x][0] != '/' and "http" not in anchor_list[x]:
				self.urls.append(domain + anchor_list[x])
			elif anchor_list[x] not in self.urls:
				self.urls.append(anchor_list[x])
		self.pull_email_links(self.raw_data)
		return self.urls
	def get_email_links(self):
		return self.email_links
	def pull_email_links(self, raw_data):
		email_list = re.findall(self.email_link_expression, str(raw_data))
		for x in range(len(email_list)):
			self.email_links.append(email_list[x])
		return self.email_links
