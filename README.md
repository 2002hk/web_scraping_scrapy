# web_scraping_scrapy_book.toscrape
## webscraping books.toscrape website using Scrapy Framework
## Libraries used
- scrapy
- ipython
- virtualenv
- mysqlconnector
## Project Structure
```bash
bookscraper/
│── venv/
│── bookscraper/               # Project module
│   ├── spiders/                # Spider definitions
│   │   ├── __init__.py
│   │   ├── bookspider.py        # Custom spider
│   ├── __init__.py
│   ├── items.py                # Define scraped data structure
│   ├── middlewares.py          # Custom middlewares
│   ├── pipelines.py            # Data processing pipelines
│   ├── settings.py             # Scrapy settings
│── scrapy.cfg                  # Scrapy configuration file
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
```
## Commands used
```bash
## to create virtual env
python -m venv venv
python venv\Scripts\activate
## to create project
scrapy startproject bookscraper
## go the spider folder
scrapy genspider bookspider books.toscrape.com
## to activate scrapy shell
scrapy shell
```
## Features of the Scraper
- Preprocessing of data done using the itempipelines removing leading and trailing spaces, removing the Rs symbol, converting string to number and viseversa.
- Used mysqlconnector to connect to the mysql database and storing the data extracted in database.
- Effective Pagination.
