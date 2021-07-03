import random
import time 
import sys 
from threading import Timer 

def speedCal(sen,initial,final):  
    words=sen.count(" ")+1 
    timediff=final-initial 
    return (words/timediff) 


def accuracyCalculation(sen,written):
    if(len(sen)==len(written)):
        count=0 
        for i in range(0,len(sen)):
            if(sen[i]==written[i]):
                count=count+1 
        return (count/len(sen)) 

    elif(len(sen)>len(written)):    
        
        return 0

    elif(len(sen)<len(written)):
        
        return 0


def collectSentence():#file handling
    sentenceslist=[]#initialization of empty list to store the sentances
    with open (r"C:\Users\91990\Desktop\typeproj\sentences_hard.txt", 'rt') as myfile:
        for myline in myfile:
            sentenceslist.append(myline.rstrip())
            
    return sentenceslist           


def playGame():    
    sentenceslist=collectSentence() 
    sentenceindex=random.randrange(0,len(sentenceslist),2)
    sen=sentenceslist[sentenceindex]
    print(sen) 
    print('\n')
    starttime=time.time() 
    st=input() 
    print('\n')
    endtime=time.time()
    if(round(accuracyCalculation(sen,st)>=0.9)):    #Checking if accuracy is greater than 90%
       print("User has very good typing skills")
       print("User accuracy is "+str(round(accuracyCalculation(sen,st)*100,2))+'%')
       print(str(round(speedCal(sen,starttime,endtime)*60,2))+" words/minute")
       print('\n')
    elif(round(accuracyCalculation(sen,st)<0.9) and round(accuracyCalculation(sen,st)>0)):
       print("Your accuracy is "+str(round(accuracyCalculation(sen,st)*100,2))+'%')
       print(str(round(speedCal(sen,starttime,endtime)*60,2))+" words/minute")
       print('\n')
    else: #Cond that accuracy will be checked only if both speed and accuracy match.
       print("Accuracy will be calculated if both the lengths are matching only ")
       print('\n')
    




while(1):
    print("Test your Typing Skills now")
    print("Choose your Option")
    print("1.Start Test")
    print("2.Exit")
   
    n=(input())
    if(n.isdigit()):
        if(int(n)<0 and int(n)>2):
            print("Invalid Option")
            sys.exit()
        elif(n=='1'):
            playGame()#calls the playGame function
        elif(n=='2'):
            sys.exit() 
        else:
            print("You selected an invalid option")
            sys.exit() #exits from the program
    else:#if you entered an invalid option other than digit
      print("You entered invalid option")
      print("Try again")
      print('\n')
