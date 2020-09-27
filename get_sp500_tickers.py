# Get the current list of S&P 500 stocks

import requests
from bs4 import BeautifulSoup

url = "https://markets.businessinsider.com/index/components/s&p_500"
tickers = []
file = open("sp500_tickers.txt", "a")
print("------------- Getting Tickers ---------------")
# loop through 10 pages, most likely wont change
for x in range(11):
    # get html from url
    print(x) # track page numbers
    response = requests.get(url + "?p=" + str(x))
    soup = BeautifulSoup(response.content, 'html.parser')
    # loop through all links in html
    for link in soup.findAll('a'):
        # parse href links to grab ticker symbols
        if "stocks" in str(link.get('href')):
            array = str(link.get('href')).split('/')
            if len(array) > 2:
                # get rid of crap items
                if "find-stocks" in array[2]:
                    continue
                elif "dividends" in array[2]:
                    continue
                else:
                    # remove the '-stock' from the ticker symbol
                    text = array[2].split("-stock")
                    # append to list
                    tickers.append(text[0])
# remove duplicates, multiple items of aapl, tsla, etc
mylist = list(dict.fromkeys(tickers))
for x in mylist:
    # write to the file
    file.write(x + "\n")

# close the file
file.close()

# EOF
