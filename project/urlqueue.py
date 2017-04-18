from queue import queue

'''
This is the url queue that will hold the list of processed urls and the queue of urls to spider. This should send messgaes to the web scraper so that it's spider_urls queue can be populated with the hrefs of the anchor tags it finds.
'''

class UrlQueue(object):
	processed_urls = [] #This is going to be a list.
	spider_urls = queue() #This is the queue.
	blacklisted_urls = [] #If there is anything that's detected by the scraper as bad, it'll get added here.
	database = None #Database object. This may need to be faked for the time being.
	def __init__(self, processed = None, spider = None, blacklist = None):
		if processed == None:
			self.processed_urls = []
		else:
			self.processed_urls = processed
		if spider == None:
			self.spider_urls = queue()
		else:
			self.spider_urls = spider
		if blacklist == None:
			self.blacklisted_urls = []
		else:
			self.blacklisted_urls = blacklist
	def add_to_processed(self, url_string):
		if not url_string in self.processed_urls:
			self.processed_urls.append(url_string)
	def add_to_spider(self, url_string):
		if not url_string in self.processed_urls:
			self.spider_urls.add(url_string)
			print(self.spider_urls)
	def add_array_to_spider(self, array_of_urls):
		for x in array_of_urls:
			if not array_of_urls[x] in self.processed_urls:
				self.spider_urls.add(array_of_urls[x])
	def add_to_blacklist(self, url_string):
		if not url_string in self.blacklisted_urls:
			self.blacklisted_urls.append(url_string)
	'''
	Todo: Add a function to send a message to the scraper. Should the object pass itself as an argument? Probably, because any queue should be able to interact with the scraper.
		We're still missing a database object to link up to. Depending on time, this may just need to be an object that acts like a database, but really is just a dictionary.
	'''
