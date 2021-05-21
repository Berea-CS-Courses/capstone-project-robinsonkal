2.A. For my testing, I plan to do an end-to-end test and a unit test. I found the unit test assignment from 226, so I’ll be using that as my framework. So for the sake of disclosure, these functions were designed from a program made by Jan Pearce and Scott Hegen. 

2.B. I specifically chose end-to-end testing because my project has many programs that must work properly in unison in order for my project as a whole to function properly  If my web scraper doesn’t communicate to the comparison program, my project will not work. If the corpus data doesn’t transfer to the comparison file, my project will not work. If the comparison program does not display information on the website correctly, then that is also a problem. Therefore an end-to-end test seems necessary to show that everything is working properly.  

3. I want to test some of the functionality of the web scraper and the Reuters corpus program. In the web scraper and the Reuters program(playing with corpora), I want to test data cleaning by entering in multiple strings and seeing if the function’s output what I expect.  I also want to test the is inside functionality, which is responsible for making sure words in the data frame do not repeat. 

For the end-to-end test, I want to go through my project completely and make sure that each program is connected to the other. Throughout the building process, I had to change file names, comment out exporting, etc. so this is important in making sure that everything works as expected. Also just keeping a better track of where things are saved and what file names are called. 




The bugs I found:

## The TRUE/FALSE bug

When running the end-to-end test I noticed this bug. I thought that maybe 1’s and 0’s were registering as TRUE and FALSE instead of numbers, but when I tested that in my unit testing that was not the case. I couldn’t figure out in what situation this would happen. I’m controlling for the case so a capital TRUE shouldn’t be showing up at all. It’s the same for FALSE too. The only thing I can figure out is that somehow these are being added after the fact. 
![image](https://user-images.githubusercontent.com/35353616/118749997-956db980-b82c-11eb-9bdc-0dc89ef6ac95.png)
![image](https://user-images.githubusercontent.com/35353616/118750024-a4546c00-b82c-11eb-8dc9-6ac43178f775.png)

![image](https://user-images.githubusercontent.com/35353616/118750051-afa79780-b82c-11eb-9a59-05b6abb29553.png)


When I compared it to data taken previously, true and false appear about the same percentage, implying that the length of the word list makes this number go up and down.

Later in the process, I saw something else weird. My comparing program wasn’t matching the word. It only showed up as NAN..That’s when I figured it out. Lower case false and true never showed up in the original scraped word list, which is suspect. I mean surely someone used the word false in 1.2 million word messages. Turns out that somewhere in the process, lower case true was turning into boolean TRUE. Possibly when making this into a (.xls file). To fix it, all I need to do is change that “TRUE” back to “true” in the comparison file. :<)



![image](https://user-images.githubusercontent.com/35353616/118750131-cfd75680-b82c-11eb-85ed-e76e9e15726b.png)



And I was able to fix the issue!

## The God Bug

While doing the end-to-end test, I got a new bug from a new data set. The word god was listed but with Nan as context. 
![image](https://user-images.githubusercontent.com/35353616/118750161-e4b3ea00-b82c-11eb-9539-ae37905ce68d.png)


It’s happening because its first appearance in the text file is the last word in a line. Because I iterated through the lines, it’s hard to get context since to get back to the post words you would have to get back to the last line. To remedy this I’m attempting to only get the pre words as context if it is at the end of a line, but I’m not sure if it’s working, and I’m running out of time.


4.
Other than that, testing went well. I tested both the corpus code and the web scraping code similarly since both programs have to clean the data in similar ways. I had to edit the functions since they weren’t designed to take in such low word counts(specifically the corpus code was specifically meant to loop 10788 times since that is the number of files available. I got around this by getting rid of the loop and passing through my test variable instead.) I also had to edit functions to return at certain points to test certain variables. In the text web scraper program, for example, I separated one function into two, to test the repeating functionality and the word cleaning functionality separately. 

![image](https://user-images.githubusercontent.com/35353616/118833263-50c73a00-b88f-11eb-974d-8ea4466a0fbd.png)


As for the comparing the data program, I couldn’t think of any unit tests that I could perform that would be worthwhile. I was actually finding many problems in the comparing file using end-to-end testing so that was most helpful for this part of the project specifically.



Finally, I finished the end-to-end test by putting new data onto my website, and fixing my exports. I completely walked through the creation of a new webscraping file, messages file, corpus file, comparison data, and the posting of that data onto the website. 

![image](https://user-images.githubusercontent.com/35353616/118749949-7ec76280-b82c-11eb-85fe-4854bdfa8c96.png)


