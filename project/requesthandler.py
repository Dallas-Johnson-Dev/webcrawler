import requests
from dataparser import dataParser
'''
Request Handler Class

This class makes a request to a url and saves the response.
The response object is from the requests library. It follows the same documentation as detailed in the requests library's documentation.
This class will also have a data parser attached that it can send the downloaded site data to to filter out the anchor tags.
'''

class requesthandler(object):
	response = None
	linkparser = dataParser()
	def __init__(self, parser=None):
		self.linkparser = parser
	def get(self, url_string):
		if not url_string == "":
			self.response = requests.get(url_string)
			return self.response
		else:
			return None
	def post(self, url_string):
		if not url_string == "":
			self.response = requests.post(url_string)
			return self.response
		else:
			return None
	def head(self, url_string):
		if not url_string == "":
			self.response = requests.head(url_string)
			return self.response
		else:
			return None
	def status_code(self):
		return self.response.status_code
	def data(self):
		return self.response.content
