from nltk.corpus import reuters
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import sys

lemmatizer = WordNetLemmatizer()





#print(reuters.fileids()[1255])
#print(len(reuters.fileids()))
stop_words = stopwords.words('english')
#print(len(reuters.categories()))


#print(reuters.words("test/17521")[:])

df = pd.DataFrame()
df['cleaned_word'] = ""
df['count_of_word']=""
df['ratio_of_use']=""

print(stop_words)
def JSON_reuters_generator(test):
    count_var=0
    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    new_r_list=[]
    #for i in range(10788):     #set to 10788 for all fileid's
    #    R_File_ID=reuters.fileids()[i]    #Sets the variable to equal file id EX: "training/9995"
        #new_r_text=reuters.words(R_File_ID)[:]
        ##print(new_r_text)
    test=test.split()
    for word in test:
            print(word)
            if word.isalpha()==True:     # males sure only words are being sent to file
                word=word.lower()
                if word not in stop_words:   # deletes stop words


                    word=lemmatizer.lemmatize(word)


                    new_r_list.append(word)#  newrlist is the list of cleaned data
    print(len(new_r_list), " words")
    count_var2=1
    count_var3=0
    for word in new_r_list:
        count_var3+=1
        print(count_var3)
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
            df.at[rowloc,'count_of_word']="1"
            #df.loc[rowloc,['count_of_word']] = 1

        if isinside>=1:
            rowloc=df[df['cleaned_word'] == word].index[0]
            valueofcountword=df.loc[rowloc].count_of_word
            valueofcountword=int(valueofcountword)
            valueofcountword=valueofcountword+1
            df.at[rowloc,'count_of_word']=valueofcountword
        count_var2+=1


    index = df. index
    number_of_rows = len(index)
    #print(number_of_rows, " this is the number of rows")
    for i in range(number_of_rows):# fills in ratio of use, divides count of word by number of words
        #df.at[index[i],'ratio_of_use']=df['count_of_word'][int((index[i]))/int(len(new_r_list))]
        df.at[index[i],'ratio_of_use']=int(df['count_of_word'][index[i]])/int(len(new_r_list))



    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(df.head(n=20000000))
    #df.to_csv(r'C:\Users\robinsonkal\Desktop\File Rueter_Data_cleaned.csv', index = False)
    return new_r_list





       # print(new_r_list)



#JSON_reuters_generator()

def testit(did_pass):
    """
    Print the result of a unit test.

    This function works correctly--it is verbatim from the textbook, Chapter 6.

    You should reuse this function anytime you are creating a custom test suite

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """

    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def JSON_reuters_generator_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the is_even() function, returning True
    only when the input is even.

    :return: None
    """
    print("\nRunning test suite().")

    # testing of positive integers
    testit(JSON_reuters_generator("bob 4 todd") ==["bob","todd"] )   #testing numbers
    testit(JSON_reuters_generator("bob todd") ==["bob", "todd"] )   #testing numbers
    testit(JSON_reuters_generator("bob 1 todd") ==["bob","todd"] )   #testing 1's, making sure they don't return TRUE or FALSE
    testit(JSON_reuters_generator("bob4 president todd") ==["president","todd"] )   #testing number in word
    testit(JSON_reuters_generator("bob ? todd") ==["bob","todd"] )   #Punctuation
    testit(JSON_reuters_generator("bob me todd you") ==["bob","todd"] )   #testing built-in stop words
    testit(JSON_reuters_generator("BOB TODD") ==["bob","todd"] )   #Capitalization





    print("Run of JSON_reuters_generator() complete.")

#file1.close()

JSON_reuters_generator_test_suite()

