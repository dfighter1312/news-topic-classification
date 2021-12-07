# https://e.vnexpress.net/news/business

import scrapy
import os
from time import sleep
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager

basedir = os.path.dirname(os.path.realpath('__file__'))

class EVnexpressSpider(scrapy.Spider):

  name = "evnexpress_links"
  allowed_domains = ["e.vnexpress.net"]
  categories = ['news']
  # categories = ['news', 'business', 'travel', 'life', 'sports', 'world'] #, 'perspectives']
  start_urls = ['https://e.vnexpress.net/news/'+category for category in categories]

  def start_requests(self):
    urls = self.start_urls
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):

    category = response.url.split("/")[-1]
    self.logger.info("Scraping E-Vnexpress by category", category)
    
    # instantiate chrome driver
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--headless")   # prevent opening chrome app

    # automatic chrome driver installation
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    driver.get(response.url)
    selector = Selector(text=driver.page_source)

    self.logger.info("***** Start opening page *****")
    self.logger.info(selector.css('h1.folder_name a::text').getall())
    self.logger.info(selector.css('a#vnexpress_folder_load_more::text').getall())

    last_height = driver.execute_script("return document.body.scrollHeight")
    SCROLL_PAUSE = 3
    MAX_SCROLL = 100  # depends on how much time you have
    i = 0
    stop = 0

    # start scrolling and expanding
    while i <= MAX_SCROLL:
      try:
        # Expand page by clicking on load-more button
        expand_button = driver.find_element_by_id("vnexpress_folder_load_more")
        expand_button.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        i += 1
        # get the selector again after each scrolling to get new content
        selector = Selector(text = driver.page_source)
        self.logger.info(f"*********** scrolling {category}-{i} ************")
        self.logger.info(len(selector.css('h2.title_news_site a.icon_commend::attr(href)').extract()))
        sleep(SCROLL_PAUSE)
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        last_height = new_height
        # if last_height == new_height and stop == 5: break
        # if last_height == new_height: stop += 1
        # else: stop = 0
      except:
        break

    self.logger.info("**** Finished scrolling ****")

    # Extract links and save
    selector = Selector(text = driver.page_source)
    contents = selector.css('h2.title_news_site a.icon_commend::attr(href)').extract()
    contents = '\n'.join(content.split('#box_comment')[0] for content in contents)

    open(f'links-2.txt', 'a').write(contents)

    driver.quit()