import unittest
from scraper import scraper

class scraper_test_cases(unittest.TestCase):
	def setUp(self):
		self.web_scraper = scraper("http://euclid.nmu.edu/~jeffhorn")
	def test_parse_site_data(self):
		print(self.web_scraper.top_level_domain)
		self.assertEqual(self.web_scraper.top_level_domain, "http://euclid.nmu.edu/~jeffhorn", "Top level domain should not be empty!")
		site_data = self.web_scraper.request_site_data(self.web_scraper.top_level_domain)
		self.assertNotEqual(site_data, "", "Site data should not be empty")
		site_urls = self.web_scraper.parse_links(site_data)
		self.assertFalse(len(site_urls) == 0, "There should be URL links that were detected!")
	def test_add_to_spider_queue(self):
		self.assertEqual(len(self.web_scraper.url_queue), 0, "Spider queue should be empty at this point!")
		self.web_scraper.add_array_to_spider_queue(self.web_scraper.parse_links(self.web_scraper.request_site_data(self.web_scraper.top_level_domain)))
		self.assertNotEqual(len(self.web_scraper.url_queue), 0, "Spider queue should be populated at this point!")
	def test_add_to_processed(self):
		self.assertEqual(len(self.web_scraper.url_queue.processed_urls), 0, "Processed URLS should be empty!")
		self.web_scraper.add_to_processed_urls("http://www.nmu.edu")
		self.assertEqual(len(self.web_scraper.url_queue.processed_urls), 1, "There should be one URL in the processed list!")
		self.assertEqual(self.web_scraper.url_queue.processed_urls[0], "http://www.nmu.edu", "Expected: \"http://www.nmu.edu\" Got: \"{0}\"".format(self.web_scraper.url_queue.processed_urls[0]))
		self.web_scraper.add_to_processed_urls(self.web_scraper.top_level_domain)
		self.assertEqual(len(self.web_scraper.url_queue.processed_urls), 2, "There should be two URLs in the processed list!")
		self.assertEqual(self.web_scraper.url_queue.processed_urls[1], "http://euclid.nmu.edu/~jeffhorn", "Expected: http://euclid.nmu.edu/~jeffhorn Got: {0}".format(self.web_scraper.url_queue.processed_urls[1]))

if __name__ == "__main__":
	unittest.main()
