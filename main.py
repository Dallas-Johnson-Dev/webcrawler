from scraper import scraper

email_scraper = scraper("{0}".format(str(input("Enter the domain you want to crawl (use quotes): "))))
email_scraper.crawl_target()
print(email_scraper.found_email_addresses)
