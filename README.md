# coding_challenge: MongoDB, Scrapy, Flask API

# Scrapping

In this project i have tried to srape the news from www.theguardian.com website and to do that i have used the framework scrapy. THe data that is scraped is stored in a hosted mongdb atlas database.

To run the scrapper:

cd to **theguardian_scrapper** directory then run the command: **scrapy crawl theguardian_news**


# API
The API homepage of theguardianScrapper can be found on **http://0.0.0.0:5000/** it shows all the data that has been scraped and collected from the mongodb database. API was built using Flask.

## Getting list of articles by article_tag, article_headline, article_url, article_timestamp.
**http://0.0.0.0:5000/\<column\>==\<value\>** , the column and value should be provided
  
### Example:
  0.0.0.0:5000/article_tag==world
  
  0.0.0.0:5000/article_headline==Johnson to press ahead with lifting Covid rules despite worry over case numbers
  

## Getting list of articles by an article_headline keyword
  **http://0.0.0.0:5000/\<keyword\>**, The keyword should be provided 
  
### Example:
  0.0.0.0:5000/children
  

