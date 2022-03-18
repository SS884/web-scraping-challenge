# Import Dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
from datetime import datetime
import os
import time



def scrape():
    # Import Splinter, BeautifulSoup, and Pandas
    from splinter import Browser
    from bs4 import BeautifulSoup as soup
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"

    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html = browser.html
    

    website_data = soup(html, "html.parser")

    element_a = website_data.select_one("div.list_text")
    

    news_title = element_a.find("div", class_ = "content_title").get_text()
    

    news_p = element_a.find("div", class_ = "article_teaser_body").get_text()
    

    url2 = "https://spaceimages-mars.com/"

    browser.visit(url2)

    html2 = browser.html
    

    website_data2 = soup(html2, "html.parser")

    button = browser.find_by_tag("button")
    

    button[1].click()

    full_image = browser.html

    full_website_image = soup(full_image, "html.parser")

    full_website_image

    mars_featured_image = full_website_image.find("img", class_ = "fancybox-image").get("src")
    

    featured_image_url = "https://spaceimages-mars.com/" + mars_featured_image
    

    mars_table = pd.read_html("https://galaxyfacts-mars.com/")[0]
    

    mars_table.columns=['Description', 'Mars', 'Earth']
    mars_table.set_index('Description', inplace=True)
    

    mars_table_html = mars_table.to_html()

    url3 = "https://marshemispheres.com/"

    browser.visit(url3)

    hemisphere=browser.html

    hemisphere_parser = soup(hemisphere, "html.parser")
    

    hemisphere_html = browser.html

    images = browser.find_by_css("a.product-item img")
    

    hemisphere_image_urls = []

    links = browser.find_by_css('a.product-item img')

    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css('a.product-item img')[i].click()
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
        hemisphere['title'] = browser.find_by_css('h2.title').text
        hemisphere_image_urls.append(hemisphere)
        browser.back()

    

    browser.quit()
    Mars_Data = {"news_title":news_title,
                "news_paragraph":news_p,
                "Featured_image":featured_image_url,
                "Facts":mars_table_html,
                "hemisphere_image_urls":hemisphere_image_urls}
    return Mars_Data 
          