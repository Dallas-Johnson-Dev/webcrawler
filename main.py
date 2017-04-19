from scraper import scraper
from flask import Flask
from flask import request

app = Flask('/')
@app.route("/", methods=['GET'])
def scrape_target():
	email_scraper = None
	target_url = request.args.get('target')
	if not target_url[len(target_url)-1] == '/':
		target_url = target_url + '/'
	email_scraper = scraper(target_url)
	return str(email_scraper.crawl_target())

if __name__ == "__main__":
	app.run()
