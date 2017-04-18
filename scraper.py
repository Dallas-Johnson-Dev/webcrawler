from requesthandler import requesthandler
from dataparser import dataParser
from urlqueue import UrlQueue
import re

class scraper(object):
	top_level_domain = ""  
	target_url = ""
	domain_expression = "((http|https)\:\/\/([a-zA-Z0-9\-]*\.)*[a-zA-Z0-9\-]*\/)"
	request_handler = data_parser = url_queue = None
	def __init__(self, domain = "", request_handler = requesthandler(), data_parser = dataParser(), url_queue = UrlQueue()):
		self.top_level_domain = re.match(self.domain_expression, str(domain)).group(0)
		self.target_url = domain
		self.request_handler = request_handler
		self.data_parser = data_parser
		self.url_queue = url_queue
		self.found_email_addresses = []
	def request_site_data(self, url):
		if url[0] == '/':
			if not (self.top_level_domain + url) in self.url_queue.processed_urls:
				self.request_handler.get(self.top_level_domain + url)
				self.add_to_processed_urls(self.top_level_domain + url)
				return self.request_handler.data()
		else:	
			if not url in self.url_queue.processed_urls and self.top_level_domain in url:
				self.request_handler.get(url)
				self.add_to_processed_urls(url)
				return self.request_handler.data()
	def parse_links(self, raw_data):
		self.add_array_to_spider_queue(self.data_parser.parse_links(raw_data, self.top_level_domain))
		return self.data_parser.parse_links(raw_data, self.top_level_domain)
	def add_to_processed_urls(self, url):
		self.url_queue.add_to_processed(url)
	def add_to_spider_queue(self, url):
		self.url_queue.add_to_spider(url)
	def add_array_to_spider_queue(self, url_list):
		for x in url_list:
			self.add_to_spider_queue(x)
	def add_to_blacklist(self, url):
		self.url_queue.add_to_blacklist(url)
	def pop_next_spider_url(self):
		return self.url_queue.get_next_spider_url()
	def pull_email_links(self, raw_data):
		return self.data_parser.pull_email_links(raw_data)
	def add_to_found_emails(self, email_list):
		if len(email_list) == 0:
			return
		for x in email_list:
			if not x in self.found_email_addresses:
				self.found_email_addresses.append(x)
	def crawl_target(self):
		#how to crawl: request site data, parse all links, parse for email links and append them to self.found_email_addresses, pop from the spider and continue the process until no urls are left.
		data = self.request_site_data(self.target_url)
		urls = self.parse_links(data)
		self.add_to_found_emails(self.pull_email_links(data))
		self.recursive_spider_crawl(len(self.url_queue)) #begin the recursive scraping here.
	def crawl_url(self, url, verbose = False):
		data = self.request_site_data(url)
		links = self.parse_links(data)
		self.add_to_found_emails(self.pull_email_links(data))
		if verbose:
			print(links)
			print(self.found_email_addresses)
	def recursive_spider_crawl(self, count): #Recursively calls itself while popping off each element in the queue and processing it.
		try:
			if count > 0:
				self.crawl_url(self.pop_next_spider_url())
				self.recursive_spider_crawl(count-1)
		except:
			pass
