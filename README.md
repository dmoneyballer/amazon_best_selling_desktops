# amazon_best_selling_desktops
A simple scraper to fetch the best selling desktops from Amazon.
## Motivation
I built this tool to scrape the Amazon best-selling desktops page every hour. I wanted to track trends in desktop sales, and this tool helps in fetching up-to-date data.
## Setup
1. Dependencies: Before you run the scraper, ensure you have all the necessary dependencies installed.

pip install -r requirements.txt

2. Running the Scraper: After installing the dependencies, you can run the scraper using:

scrapy crawl desktops -o desktops.json
## Deployment
I've set this up on my Raspberry Pi to run as a cron job every hour. This ensures that I always have fresh data. 
