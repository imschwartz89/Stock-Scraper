# googleTest.py Scraper for Google
googleTest.py scrapes Google's search engine to get stock prices

## Fixing the "Gibberish Has Changed" Problem
To solve this problem you will need to open the returned HTML source file and find the price of the ticker. 

To do this follow these instructions:
- Run the command (python3 refers to Python 3):
<br />`$ python3 googleTest.py -p -o AAPL.html`
<br />This will create a file named ***AAPL.html*** with the source code for that page.
- Open ***AAPL.html*** using browser
- Find the stock price for AAPL (on the browser page you just opened)
- Right click on the browser and open the source code for the page
- Ctrl+F and enter the stock price you found on the page
- Right before the stock price should be: `"><div><div class="{gibberish}">`
<br />Where **{gibberish}** is the ***new gibberish*** to put in the CSV file
- Copy and paste the ***new gibberish*** over the ***old gibberish*** which is right after the "Price" header in the CSV file

***NOTE: If that gibberish is the same as what is in the CSV file, then there is a different problem. You probably will need to check your CSV file.***
