import time
import random
a_music={}
new_music={}
l=[]


'''def sort():
    l=[]
    for i in a_music:
        l.append(a_music[i][5])
        l1.append(i)
        
    sorted(l)
        new_music=a_music.copy()
    print(new_music)'''
                


def generate_isrc():
    l=[]
    s1=''
    r1=random.randint(0,25)
    r2=random.randint(0,25)
    r3=random.randint(0,25)
    r4=str(random.randint(10,99))
    r5=str(random.randint(0,9))

    for i in range(65,91):
        l.append(chr(i))
    
    s1+=l[r1]
    s1+=r4
    s1+='-'
    s1+=r5
    s1+=l[r2]
    s1+=l[r3]
    
    return s1
    
def add_data():
    ch=''
    while(ch.lower()!='n'):
        isrc=generate_isrc()
        s_name=input("\n\t\t Enter Song Name ")
        g_name=input("\n\t\t Enter Genre of the Song ")
        a_name=input("\n\t\t Enter Artist's Name ")
        y_rl=int(input("\n\t\t Enter Year of Release "))
        tempo=input("\n\t\t Enter Tempo of the Song ")
        streams=int(input("\n\t\t Enter number of streams "))
        a_music[isrc]=[s_name,g_name,a_name,y_rl,tempo,streams]
                
        ch=input("\n\t\t Do you want to add more songs (Y/N)? ")
    print("\t\t\tAdding Now! Please wait:)")
    time.sleep(1.5)
    for i in a_music:
        print("\n\t\t\t ISRC of the Song is- ", i)
        
        
def view_data():
    if(a_music!={}):
        print("\nISRC\t\tSong\t\tGenre\t\tArtist\t\tYoR\t\tTempo\t\tStreams")
        for i in a_music:
            print("\n",i,end='\t\t')
            for j in a_music[i]:
                print(j,end='\t\t')
    else: 
        print("\n\t\t\tNo Data to Display!")


        
def search():
    flag=0
    print("\n\t\t\tSearch on the basis of:\n\t\t\t\t 1. ISRC\n2. Song Name\n3. Artist\n4. Year of Release\n5. Tempo\n6. Genre")
    ch1=int(input("\n\t\t\t\tEnter from the above options "))
    if(ch1==1):
        is_rc=input("\n\t\t\tPut in the ISRC, which you want to search ")
        for i in a_music:
            if(is_rc==i):
                print("\n\t\tISRC\tSong Name\tArtist")
                print(i,a_music[i][0],a_music[i][2],sep='\t')
                flag=1
            
        if(flag==0):
            print("\n\t\t\tISRC doesn't match our records:/")
                
                
    elif(ch1==2):
        song=input("\n\t\t\tPut in the song name ")
        for i in a_music:
                if(song==a_music[i][0]):
                    print("\n\t\tSong Name\tISRC\tArtist")
                    print(a_music[i][0],i,a_music[i][2],sep='\t')
                    flag=1
            
        if(flag==0):
            print("\n\t\t\tSong Name doesn't match our records:/")
    
    elif(ch1==3):
        artist=input("\n\t\t\tPut in the artist's name ")
        for i in a_music:
            if(a_music[i][2]==artist):
                print("\n\t\tArtist\tISRC\tSong Name")
                print(a_music[i][2],i,a_music[i][0],sep='\t')
                flag=1
                
        if(flag==0):
            print("\n\t\t\tArtist doesn't match our records:/")
    
    elif(ch1==4):
        y_o_r=int(input("\n\t\t\tPut in the year of release "))
        for i in a_music:
            if(a_music[i][3]==y_o_r):
                print("\n\t\tYoR\tISRC\tSong Name")
                print(a_music[i][3],i,a_music[i][0],sep='\t')
                flag=1
                
        if(flag==0):
            print("\n\t\t\tYoR doesn't match our records:/")
        
    elif(ch1==5):
        tempo=input("\n\t\t\tEnter tempo ")
        for i in a_music:
            if(a_music[i][4]==tempo):
                print("\n\t\tTempo\tISRC\tSong Name")
                print(a_music[i][4],i,a_music[i][0],sep='\t')  
                flag=1
                
        if(flag==0):
                print("\n\t\t\tTempo doesn't match our records:/")
        
    elif(ch1==6):
        genre=input("\n\t\t\tEnter genre ")
        for i in a_music:
            if(a_music[i][1]==genre):
                print("\n\t\tGenre\tISRC\tSong Name")
                print(a_music[i][1],i,a_music[i][0],sep='\t') 
                flag=1
                
        if(flag==0):
            print("\n\t\t\tGenre doesn't match our records:/")
            
            
def update_all(isrc):
        s_name=input("\n\t\t Enter Song Name ")
        g_name=input("\n\t\t Enter Genre of the Song ")
        a_name=input("\n\t\t Enter Artist's Name ")
        y_rl=int(input("\n\t\t Enter Year of Release "))
        tempo=input("\n\t\t Enter Tempo of the Song ")
        streams=int(input("\n\t\t Enter number of streams "))
        a_music[isrc]=[s_name,g_name,a_name,y_rl,tempo,streams]

    
                
def update_records():
    flag=0
    is_rc=input("\n\t\t\tPut in the ISRC, for which you want to update records ")
    for i in a_music:
        if(is_rc==i):
            flag=1
            print("\n\t\tUpdation starting NOW")
            time.sleep(1.5)
            ch=input("\n\t\tDo you want to update all the records (Y/N) ")
            
            if(ch.lower()=='y'):
                update_all(is_rc)
                
            else:    
                print("\n\t\t\tWhat do you want to update:\n\t1. Song Name\n2. Artist\n3. Year of Release\n4. Tempo\n5. Genre\n6. Streams")
                ch2=int(input("\n\t\t\t\tEnter from the above options "))
            
                if(ch2==1):
                    s_name=input("\t\t\tEnter New Song Name ")
                    a_music[i][0]=s_name
            
                elif(ch2==2):
                    artist=input("\t\t\tEnter New Artist Name ")
                    a_music[i][2]=artist
                
                elif(ch2==3):
                    y_o_r=int(input("\t\t\tEnter New Year of Release "))
                    a_music[i][3]=y_o_r
            
                elif(ch2==4):
                    tempo=input("\t\t\tEnter New Tempo ")
                    a_music[i][4]=tempo
            
                elif(ch2==5):
                    g_name=input("\t\t\tEnter New Genre ")
                    a_music[i][2]=g_name
                
                elif(ch2==6):
                    streams=int(input("\t\t\tEnter New Number of Streams "))
                    a_music[i][5]=streams
            
                else:
                    print("\n\t\tYou've entered wrong choice ")   
                    
    if(flag==0):
        print("\n\t\t\tISRC doesn't match our records:/")
    print("\n\t\t\tUpdation Successful!")

def remove_records():
    flag=0
    ch=input("\n\t\tEnter ISRC of the record which you wanna delete ")
    for i in a_music:
        if(i==ch):
            flag=1
            a_music.pop(i)
            break
    if(flag==0):
        print("\n\t\tIncorrect ISRC entered")
    print("\n\n\t\tSuccessfully Removed")






def choice(ch3):
    if(ch3.lower()=='a'):
        add_data()
    elif(ch3.lower()=='b'):
        view_data()
    elif(ch3.lower()=='c'):
        search()
    #elif(ch3.lower()=='d'):
        #sort()
    elif(ch3.lower()=='d'):
        remove_records()
    elif(ch3.lower()=='e'):
        update_records()
    else:
        print("\n\t\t\t\t\tsorry! wrong choice entered")

