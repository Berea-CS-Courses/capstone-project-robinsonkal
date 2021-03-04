

# Digital Dogwhistle PSA Website Decomposition

_____


# Web Scraper Application


Using an open-source social media web scraper

Exports full messages to a text document(JSON)

4chan is ripe with problematic language, but it might be difficult to get

Found a few 4chan threads

Might have to create my own webscraper later, probably will use premade one in prototyping phase

If so, I will utilize python libraries URL Lib and Beautiful Soup to do so, content will extract to JSON file

Will run every month, at least



# Python program


### IMPORTS: full scraped message from a text document (JSON)
Tracks words being used most frequently in Json File, lists them

application needs to be able to filter out words such as the, though, etc.

Python text analysis library? Keyword Extraction?


Scraping other websites for text analysis comparison ie this word only shows up this percent in other websites.

Program needs to be able to flag overused words.


will be utilizing Python Pandas, dataframes, series


### EXPORTS: dog whistle, likelihood, a message in context, and location to a JSON file


	Function1: Takes in messages
			Needs to store the message for later
			(Probably into a dataframe?)
			Needs to differentiate between words such as The
			Exports: list of most used words

	Function2: Takes in list of most used words
			Possibly comparing it to percentage of use in other sites
			If I do this I will probably need to make my own scraper
			Will probably need to scrape from NOW corpus
			How often are these words used in regular online speech?
			Exports: list of words with the percentage of difference.

	Function 3. Matches words with messages and origin
			Puts data into data frame
			Exports dataframe to database or JSON file









# Website
Another program that utilizes Altair graphical capabilities, for web page

Shows data from the JSON file

Voyant inspired graphical interfaces, seperated by date

Webhosting

Basic Front end design


Python and Flask




