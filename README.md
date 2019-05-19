# GooglePlayScrapperByCategory

This project is a Google Play crawler based on category. Pyhton Scrapy is used to implement scrapper.
To run use the bellow command:
cd spiders
scrapy crawl gplaymedical -o output.json

This code by default crawls Only Medical category apps. It can be changed to crawl all/ specific category apps. Right now it crawls 
app name, link, description, rating, genre and price attribute values. It can be modified to collect other app specific datas.
