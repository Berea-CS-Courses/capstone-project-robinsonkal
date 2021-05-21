import pandas as pd
import altair as alt
import time
import re
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
print(number_of_rows3)
time.sleep(5)
loopnum=(number_of_rows3-50)
print(loopnum)
time.sleep(5)
for i in range(loopnum):
    dropnum=(number_of_rows3-i)
    print(dropnum)
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





