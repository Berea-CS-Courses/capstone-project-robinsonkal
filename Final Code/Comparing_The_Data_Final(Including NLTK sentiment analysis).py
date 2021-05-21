import pandas as pd
import altair as alt
import time
import re
import nltk
from nltk.corpus import webtext
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import word_tokenize
import random
import re, string
from nltk import classify
from nltk import NaiveBayesClassifier

stop_words = stopwords.words('english')
teststring="My groove is a different story, and I want to plant a tree. It's the funky beats, really. My sex appeal is really confusing, and I want to get more done. Seeing fine style, so it goes.My job is fantastic, and I want to live worry free. Looking for grand heroes, please. I hate skittles, they are terrible at driving!"

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')

tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

#print(tweet_tokens)
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence

#print(lemmatize_sentence(tweet_tokens[0]))



def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())

    return cleaned_tokens


#print(remove_noise(tweet_tokens[0], stop_words))

positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

positive_cleaned_tokens_list = []
negative_cleaned_tokens_list = []

for tokens in positive_tweet_tokens:
    positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

for tokens in negative_tweet_tokens:
    negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))


#print(positive_tweet_tokens[500])
#print(positive_cleaned_tokens_list[500])


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

all_pos_words = get_all_words(positive_cleaned_tokens_list)

freq_dist_pos = FreqDist(all_pos_words)
#print(freq_dist_pos.most_common(20))

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

positive_dataset = [(tweet_dict, "Positive")
                     for tweet_dict in positive_tokens_for_model]

negative_dataset = [(tweet_dict, "Negative")
                     for tweet_dict in negative_tokens_for_model]

dataset = positive_dataset + negative_dataset

random.shuffle(dataset)

train_data = dataset[:7000]
test_data = dataset[7000:]

classifier = NaiveBayesClassifier.train(train_data)


alt.renderers.enable('altair_viewer')


#new_df = pd.DataFrame()
#new_df['potential_dog_whistle'] = ""
#new_df['count_of_use']=""
#new_df['ratio_of_use']=""
file1 = open("Messages.txt","r+")



df_fourchandata = pd.read_excel (r'C:\Users\robinsonkal\Documents\File fourchan_Data_pol_final.xls')
#print (df_fourchandata)

df_Reuter_Data = pd.read_excel (r'C:\Users\robinsonkal\Desktop\File Rueter_Data_cleaned_copy.xls')
#print(df_Reuter_Data)

new_df=pd.merge(df_fourchandata, df_Reuter_Data, on="cleaned_word")
true_df = pd.DataFrame()
#true_df['greater_than_x']=""
#print(new_df)

index1 = new_df. index
number_of_rows1 = len(index1)
count1=0
#print(number_of_rows, " this is the number of rows")
#for i in range(number_of_rows):# Goes through the rows in new_df
for i in range(number_of_rows1):# Goes through the rows in new_df
    if new_df["ratio_of_use_webscraper"][i]*.05>new_df["ratio_of_use"][i]: #if one ratio is much large than the other
       # true_df["greater_than_x"].append(new_df["cleaned_word"][i])
        true_df.at[count1, "greater_than_x"] = str((new_df["cleaned_word"][i])).lower()  #then add that word to a new dataframe
        true_df.at[count1, "word_count"] = (new_df["count_of_word_webscraper"][i])  #then add that word count to a new dataframe
        count1+=1
        #print("true")
        #print(new_df["cleaned_word"][i])

index2 = true_df.index
number_of_rows2 = len(index2)
for i in range(number_of_rows2):
    count2=0
    print(i)

    file1.close()
    file1 = open("Messages.txt","r+")
    pre_words=[]
    post_words= []
    for line in file1:
        newline=0
        countword=0
        if count2<2:
            newstring = re.findall(r"[\w']+", line)    #seperates messages into words and deals with punctuation
            maxlen=len(newstring)
            for word in newstring:
                countword+=1
                premessagecontext=""
                #print(word)

                if newline==0:
                    pre_words.append(word)
                    if len(pre_words)>14:
                        pre_words.pop(0)
                        #print(pre_words)
                        #time.sleep(1)
                        premessagecontext=" ".join(pre_words)
                if newline==1:
                    post_words.append(word)
                    if len(post_words)>14:
                        #post_words.pop(0)
                        #print(len(post_words))
                        for lis1word in range(len(post_words)):
                            print(lis1word)
                            if post_words[lis1word]=="xe2":
                                post_words[lis1word]=""
                            if post_words[lis1word]=="x80":
                                post_words[lis1word]=""
                            if post_words[lis1word]== "x99d":
                                post_words[lis1word]="'d"
                            if post_words[lis1word]== "x99s":
                                post_words[lis1word]="'s"
                            if post_words[lis1word]== "x99m":
                                post_words[lis1word]="'m"
                            if post_words[lis1word]== "x99nt":
                                post_words[lis1word]="'nt"
                            if post_words[lis1word]== "x99t":
                                post_words[lis1word]="'t"

                        for lis2word in range(len(pre_words)):
                            if pre_words[lis2word]=="xe2":
                                pre_words[lis2word]=""
                            if pre_words[lis2word]=="x80":
                                pre_words[lis2word]=""
                            if pre_words[lis2word]== "x99d":
                                pre_words[lis2word]="'d"
                            if pre_words[lis2word]== "x99s":
                                pre_words[lis2word]="'s"
                            if pre_words[lis2word]== "x99m":
                                pre_words[lis2word]="'m"
                            if pre_words[lis2word]== "x99nt":
                                pre_words[lis2word]="'nt"
                            if pre_words[lis2word]== "x99t":
                                pre_words[lis2word]="'t"


                        #print(pre_words)
                        #print(post_words)
                        current_word=(pre_words[13])
                        pre_words[13]="* "+current_word+ " *"
                        postmessagecontext=" ".join(post_words)
                        premessagecontext=" ".join(pre_words)
                        #print(premessagecontext)
                        #print(postmessaecontext)
                        messagecontext=premessagecontext+" " +postmessagecontext
                        #print(messagecontext)
                        #time.sleep(5)
                        raw_message = messagecontext

                        custom_tokens = remove_noise(word_tokenize(raw_message))

                        #print(classifier.classify(dict([token, True] for token in custom_tokens)))
                        true_df.at[i, "Sentiment_Analysis"] = (classifier.classify(dict([token, True] for token in custom_tokens)))
                        true_df.at[i, "context1"] = messagecontext
                        newline+=1
                        count2+=1


                messagecontext=" ".join(pre_words)
                if true_df["greater_than_x"][i] == word.lower() and newline==0:
                    #context=file1[count2]
                    newline=1
                    if countword==maxlen:
                        temppostmess=" ".join(post_words)
                        true_df.at[i, "context1"] = temppostmess

                    #time.sleep(4)
                    #print(word)
                    #print(line)
                    #true_df.at[i, "context1"] = messagecontext

                    count2+=1
       # if count2==1:
       #     newstring = re.findall(r"[\w']+", line)    #seperates messages into words and deals with punctuation
       #     for word in newstring:
       ##         time.sleep(1)
        #        print(word)
                #post_words.append(word)
                #if len(post_words)>8:
                #    post_words.pop(0)
                #    #print(pre_words)
                #    #time.sleep(1)




newtrue=true_df
newtrue.sort_values(by=['word_count'], inplace=True, ascending=False)
newtrue.reset_index(drop=True, inplace=True)
index3=newtrue.index
number_of_rows3=(len(index3)-1)
#print(number_of_rows3)
time.sleep(5)
loopnum=(number_of_rows3-50)
#print(loopnum)
time.sleep(5)
for i in range(loopnum):
    dropnum=(number_of_rows3-i)
    #print(dropnum)
    newtrue=newtrue.drop(dropnum)



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#print(true_df.head(n=20000000))
print(newtrue.head(n=20000000))


#true_df.to_csv(r'C:\Users\robinsonkal\Desktop\File final_chart_data.csv', index = False)
time.sleep(10)

    #df.at[index[i],'ratio_of_use']=df['count_of_word'][int((index[i]))/int(len(new_r_list))]
    #new_df.at[index[i],'greater_than_x']= int(new_df['count_of_word'][index[i]])

chart=alt.Chart(newtrue).mark_point().encode(
    alt.X('greater_than_x'),
    alt.Y('word_count')
)

html=newtrue.to_html()
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
chart.save('chart.html')
chart.show()
file1.close()





