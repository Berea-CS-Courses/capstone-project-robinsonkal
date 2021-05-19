from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
import requests
import time
from nltk.corpus import stopwords

import pandas as pd

import re
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
stop_words.extend(['http','org','com','www','lt','htm','html','https','youtu'])

print(stop_words)
file1 = open("Messages_pol.txt","a")
file1.truncate(0)

df = pd.DataFrame()
df['cleaned_word'] = ""
df['count_of_word_webscraper']=""
df['ratio_of_use_webscraper']=""

text=''



def webscraper(Runtime):
    newstring=''
    new_output_list = []
    output = ''
    archive_column_numbers=[]
    for i in range(Runtime):

        print(i)
        #if i==1:
        #    i=2       ##I don't think i'll be needing this anymore
        url = 'https://boards.4channel.org/pol/archive'
        #url = 'https://boards.4chan.org/pol/'+str(i)
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')

        #text = soup.find_all("td",text=True)
        rows = soup.find_all("tr")    # finds the numbers for the archives url
        for row in rows:
            first_column = row.findAll('td')[0].contents
            archive_column_numbers.append(first_column)    # finds the numbers for the archives url, throws into list
        archive_column_numbers.pop(0)
        count_of_archive_numbers=len(archive_column_numbers)
        print (count_of_archive_numbers)

        #count_down=count_of_archive_numbers
        count_down=2999
        string1=''
        #for i in range(count_of_archive_numbers):     # takes last number in list, goes to each irl in list

        for i in range(2999):      #the amount of messages you want. up to 3000
            try:
                if i == 500:
                    time.sleep(300)
                if i == 1000:
                    time.sleep(300)
                if i == 1500:
                    time.sleep(300)
                if i == 2000:
                    time.sleep(300)
                if i == 2500:
                    time.sleep(300)
                output=''
                string1=''
                url=''
                archive_attach=archive_column_numbers[count_down]
                count_down-=1
                for ele in archive_attach:     #makes list into string for url
                    string1+=archive_attach[0]
                print("pass", i)
                url = 'https://boards.4channel.org/pol/thread/'+str(string1)
                print(url)
                res = requests.get(url)
                print(res)
                html_page = res.content
                soup = BeautifulSoup(html_page, 'html.parser')
                text = soup.find_all(text=True)
                print(text)
            except:
                text=""
                input("An error occured while scraping. Type anything to continue")    #stops it from running if error occurs(for internet issues)


           # blacklist = [
            #    '[document]',
            #    'noscript',
            #    'header',
            #    'html',
            #    'meta',
            #    'head',
            #    'input',
            #    'script',
            #    # there may be more elements you don't want, such as "style", etc.
            #]

            for t in text:
                #print(t.parent.name)

                if t.parent.name == "blockquote":
                    output += '{} '.format(t)

            print(output)
            output2=output
            output2 = output2.encode("utf-8")
            print("v")


            file1.write(str(output2)+'\n')



            newstring+=output
            #print("this is new string", newstring)
            time.sleep(5)

    #output=output.split()            #seperates messages into words

    newstring = re.findall(r"[\w']+", newstring)    #seperates messages into words and deals woth punctuation

# printing result
    #print("The list after performing split functionality : " , newstring)


    for word in newstring:
        if word.isalpha()==True:     # makes sure only words are being sent to file
            word=word.lower()
            if word not in stop_words:   # deletes stop words
                word=lemmatizer.lemmatize(word)
                new_output_list.append(word)#  new output list is the list of cleaned data

    #print(new_output_list)

    print(len(new_output_list), " words")
    time.sleep(5)
    count_var2=1
    count_var3=0
    for word in new_output_list:
        count_var3+=1
        print(count_var3, " out of", len(new_output_list))
        #isinside= word in df.cleaned_word
        #count_var3+=1
        isinside = len(df[df['cleaned_word'] == word])
        if isinside<1:
            #df['cleaned_word'][count_var]=word
            df.at[count_var2,'cleaned_word']=word
            rowloc=df[df['cleaned_word'] == word].index[0]
            #print(rowloc)
            #rowloc=df.loc[df['cleaned_word'] == word]
            #print(rowloc)
            df.at[rowloc,'count_of_word_webscraper']="1"
            #df.loc[rowloc,['count_of_word']] = 1
        if isinside>=1:
            rowloc=df[df['cleaned_word'] == word].index[0]
            valueofcountword=df.loc[rowloc].count_of_word_webscraper
            valueofcountword=int(valueofcountword)
            valueofcountword=valueofcountword+1
            df.at[rowloc,'count_of_word_webscraper']=valueofcountword
        count_var2+=1


    index = df. index
    number_of_rows = len(index)
    #print(number_of_rows, " this is the number of rows")
    for i in range(number_of_rows):# fills in ratio of use, divides count of word by number of words
        #df.at[index[i],'ratio_of_use']=df['count_of_word'][int((index[i]))/int(len(new_r_list))]
        df.at[index[i],'ratio_of_use_webscraper']=int(df['count_of_word_webscraper'][index[i]])/int(len(new_output_list))



    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(df.head(n=20000000))
    df.to_csv(r'C:\Users\robinsonkal\Desktop\File fourchan_Data_pol_run2.csv', index = False)



webscraper(1)

file1.close()
