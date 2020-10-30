# Stock-Scraper
Python scripts that can scrape stock, ETF, Mutual Fund price values from search engines

## Requirements
Python 3 (tested on 3.6.8)
<br /><br />Libraries (come standard in Python 3):
- requests
- csv
- argparse
- os.path

## Background
***NOTE: All data on website is made up for testing purposes***
<br /><br />&nbsp;&nbsp;&nbsp;&nbsp;I wanted to make something that could quickly tell a user what their portfolio was worth without requiring them to log on anywhere. Before creating this web scraper I tried using the following libraries: quandl, yahoo_fin, and yfinance. They did not have the desired results, so I tried using the financialmodelingprep API, but that did not have all the stock tickers available. It also requires an API key now. 
<br />&nbsp;&nbsp;&nbsp;&nbsp;So, that is when I tried scraping Google's search engine. The downside is that it requires a gibberish identifier to be able to determine what the price was. It seems to remain constant for the requests library, but if you were trying to find it in the source code of your HTML returns it will change. (The -p flag was designed to combat the gibberish changing, this will be discussed on the Google readme). Therefore, I wanted an easier solution that would not require the user to need to go through the HTML source code to find the new gibberish in the event that it does change.
<br />&nbsp;&nbsp;&nbsp;&nbsp;I began by looking up other search engines, I went through many, but the only ones that had potential were Yahoo, Bing, and OneSearch. Bing  was not useful as the price value was not available in the HTML source code. Yahoo had plenty of information, but it would have been a chore to parse through the HTML code, so I decided to skip that one. OneSearch had a consistent identifier which made it the obvious choice.
<br />&nbsp;&nbsp;&nbsp;&nbsp;I also quickly tried scraping from MarketWatch and WSJ, but they have measures to prevent scraping.


## Script Files
**oneSearch/oneSearch.py** - uses OneSearch's search engine to scrape stock data
<br />**google/googleTest.py** - uses Google's search engine to scrape stock data

## Miscellaneous Files
See these folders for the files...
<br />**csvFiles/** - CSV files used to create the output text files using **oneSearch.py**
<br />**outputs/** - the outputs after running **oneSearch.py** on given data from **csvFiles/**

## How to Use
(Coming soon)

## Future Work
- [ ] make a main python script that holds all the functions and then user can choose between search engines by command args
- [ ] make simple game that allows user to start with a certain amount of funds and then they can buy and sell at current price
- [ ] make print option that displays number of Shares and the Current Price
