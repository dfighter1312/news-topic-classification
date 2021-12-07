# Crawler

Implementations of crawler.

## Required packages

- scrapy
- webdriver-manager
- selenium

## Run crawler

The process consists of two steps:

### Retrieve links from the sites

```
$ cd tutorial
$ scrapy crawl evnexpress_links
```

The crawler iterates over the major news categories of E-Vnexpress ('news', 'business', 'travel', 'life', 'sports', 'world'),
scrolling down and expanding the list using Selenium's driver interaction. Specify the maximum scrolling depth in `tutorial/spiders/evnexpress_spider.py`.

### Crawl the content of each news article

```
$ scrapy crawl evnexpress_contents -o items.csv
```

The scraper will use the scraped links from `links.txt` and save the result into `item.csv`