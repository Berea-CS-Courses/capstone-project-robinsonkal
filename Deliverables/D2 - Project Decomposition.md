

# Digital Dogwhistle PSA Website Decomposition

_____


# Web Scraper Python Program


I am developing a self made webscraper

Exports full raw text data(social media posts) to a text document

4chan is ripe with problematic language, will be one of the websites used to detect dogwhistle-language

I utilize python libraries URL Lib and Beautiful Soup to do webscraping

Will run every month, at least. Considering every two weeks.

# Python program that cleans and processes data, (data cleaning pipeline)
This program gets the data ready to be analyzed by NLTK processes.

Will remove un-needed data

Will normalize case of text

Will split up sentences into better to process bits

Will potentially filter out stop-words

Will potentially filter out data

Will export cleaned data to next process


# Python program that analyzes text and identifies dogwhistles


### IMPORTS: full scraped message from a text document 

application needs to be able to filter out words such as the, though, etc.

Python text analysis library. Specifically the NLTK (natural language tool kit).

NLTK processes such as sentiment analysis will be used on data.

Compares words most used to a corpus available from the NLTK.

Program needs to be able to flag overused words.

will be utilizing Python Pandas, dataframes, series


### EXPORTS: potential dog whistles to a JSON file


	Process1:Takes in Cleaned data
			Exports: Data that has been analyzed through NLTK processes, such as sentiment analysis
	
	Process2: Takes in messages
			Exports: list of most used words

	Process3: Takes in list of most used words
			Possibly comparing it to percentage of use in other word corpus's
			Identifying often these words used in regular online speech, to imply dogwhistle usage.
			Exports: list of words with the percentage of difference.



# Python graphing program
This python program will be sending pictures of graphical representations of data to the website

Will be suing a python library called altair for graphing capabilities

Will also be matching dog-whistles with contextual data to be shown on the website

Sends matched information to a JSON document that the website accesses

# JSON files
Json files will be used to organize the transfer of data

For example, between the graphing program and website will be a JSON organizational file


# Website
Shows data from the JSON file

Voyant inspired graphical interfaces, seperated by date

Webhosting

Basic Front end design

Python and Flask




