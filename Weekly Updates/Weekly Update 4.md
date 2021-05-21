# Update for the 4th week of self reports

## 1.
- This week I finished some of my goals, but I ran into some problems
- I successfully instituted lemmization into both the webscraping and corpus code. 
- I tested out other forms of cleaning, and ran some tests, adding certain words/phrases to the stop words such as http, etc..
- I reran both programs and was able to get a cleaner corpus data set, but havent gotten a new 4chan data set yet.
- I added quality of life changes in order to solve certain problems that I've been having

## 2. 

- When rerunning my two programs, I ran into some problems in my webscraper code

- In the original run I accidentally saved over the messages text file which held the context for all the data

- This run's webscraper data also wouldn't move into a new dataframe. I think because of encoding issues.

- In the next run, my computer disconnected from the internet mid scrape. Since it takes so long to run, this is a big deal

- To hopefully remedy this issue in the future, I set up a try and except error handle in the scraping loop. Now if there is an error in this process the program will pause until something is typed as an input, which gives me time to reconnect to internet.

- On my third run, the webscraper just stopped. At the time I was taking an exam on moodle. Maybe something built in to the computer to stop webscrapers while taking moodle quizzes? I honestly don't know.

- To keep track of the word proccessing I added a "# of word out of total numbers" print statement, just so I know where the program is in the process.

- I'm currently rurunning the code and it may or may not be ready for next class


## 3. 

- I want to get to processing this new data, by comparing the data in excel. This process will be replicated in a python program later.  -1 days

- I want to work some with the graphing program, and replicate the data processing from the comparison excel sheet.    -3 days

- I want to make progress on another part of my project, i.e. Sentiment analysis or maybe even the website    -2 days

## 4.
- I'm using beautiful soup and python pandas

- NLTK sentiment analysis along with other NLTK tools
