import time
import random
import os
import pickle
import license1 as l
a_music={}
new_music={}



'''def sort():
    l=[]
    for i in a_music:
        l.append(a_music[i][5])
        l1.append(i)
        
    sorted(l)
        new_music=a_music.copy()
    print(new_music)'''
                

def read(Id,Pass):
    flag=0
    f=open('cred.dat','rb')  
    try:
        while(True):
            g=pickle.load(f)
            for i in g:
                if(i==Id and g[i]==Pass):
                    flag=1
                    break
                
    except:
        f.close()

    if(flag==0):
        print("\n\t\t\tWrong ID or Password")
    else:
        print("\n\t\tSigning in... PLEASE HOLD YOUR HORSES🙏🏻")
        time.sleep(1.5)
        print("\n\t\t\tWELCOME AGAIN ",Id)#delay of 1.5 seconds
        time.sleep(1.5)
        l.menu()



def validate(Id):
    f=open('cred.dat','rb')
    flag=1
    
    try:
        while(True):
            g=pickle.load(f)
            for i in g:
                if(i==Id):
                    flag=0
                    break
    except:
        pass

    f.close()
    return flag

    
def write(Id,Pass):
    flag=1
    d={}
    f1=open('flag1.txt','r+')
    f=open('cred.dat','ab')
    if(int(f1.read(1))==0):
        d[Id]=Pass
        pickle.dump(d,f)
        print("\n\t\t\t     Account Successfully Created!")
        f1.seek(0)
        f1.write("1")

    else:
        if(validate(Id)==0):
            print("\nID exists already")
            
        else:
            d[Id]=Pass
            pickle.dump(d,f)
            print("\n\t\t\t     Account Successfully Created!")
        

    f1.close()
    f.close()


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
    f=open('data.dat','ab')
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
        pickle.dump(a_music,f)
                
        ch=input("\n\t\t Do you want to add more songs (Y/N)? ")
    print("\t\t\tAdding Now! Please wait:)")
    time.sleep(1.5)
    for i in a_music:
        print("\n\t\t\t ISRC of the Song is- ", i)
        
        
def view_data():
    f=open('data.dat','rb')
    flag=0
    try:
        print("\nISRC\t\tSong\t\tGenre\t\tArtist\t\tYoR\t\tTempo\t\tStreams")
        while(True):
            g=pickle.load(f)
            if(g):
                flag=1
                for i in g:
                    print("\n",i,end='\t\t')
                    for j in g[i]:
                        print(j,end='\t\t')
    except:
        f.close()

    if(flag==0):
        print("\n\t\t\tNo Data to Display!")


        
def search():
    flag=0
    f=open('data.dat','rb')
    print("\n\t\t\tSearch on the basis of:\n\t\t\t\t 1. ISRC\n2. Song Name\n3. Artist\n4. Year of Release\n5. Tempo\n6. Genre")
    ch=int(input("\n\t\t\t\tEnter from the above options "))

    try:
        while(True):
            g=pickle.load(f)
            if(g!=''):
                if(ch==1):
                    isrc=input("\n\t\t\tPut in the ISRC, which you want to search ")
                    for i in g:
                        if(isrc==i):
                            print("\n\t\tISRC\tSong Name\tArtist")
                            print(i,g[i][0],g[i][2],sep='\t')
                            flag=1
                            break
            
                    if(flag==0):
                        print("\n\t\t\tISRC doesn't match our records:/")
                
                
                elif(ch==2):
                    song=input("\n\t\t\tPut in the song name ")
                    for i in g:
                        if(song==g[i][0]):
                            print("\n\t\tSong Name\tISRC\tArtist")
                            print(g[i][0],i,g[i][2],sep='\t')
                            flag=1
                            break
            
                    if(flag==0):
                        print("\n\t\t\tSong Name doesn't match our records:/")
    
                elif(ch==3):
                    artist=input("\n\t\t\tPut in the artist's name ")
                    for i in g:
                        if(g[i][2]==artist):
                            print("\n\t\tArtist\tISRC\tSong Name")
                            print(g[i][2],i,g[i][0],sep='\t')
                            flag=1
                            break
                
                    if(flag==0):
                        print("\n\t\t\tArtist doesn't match our records:/")
    
                elif(ch==4):
                    y_o_r=int(input("\n\t\t\tPut in the year of release "))
                    for i in g:
                        if(g[i][3]==y_o_r):
                            print("\n\t\tYoR\tISRC\tSong Name")
                            print(g[i][3],i,g[i][0],sep='\t')
                            flag=1
                            break
                
                    if(flag==0):
                        print("\n\t\t\tYoR doesn't match our records:/")
        
                elif(ch==5):
                    tempo=input("\n\t\t\tEnter tempo ")
                    for i in g:
                        if(g[i][4]==tempo):
                            print("\n\t\tTempo\tISRC\tSong Name")
                            print(g[i][4],i,g[i][0],sep='\t')  
                            flag=1
                            break
                
                    if(flag==0):
                        print("\n\t\t\tTempo doesn't match our records:/")
        
                elif(ch==6):
                    genre=input("\n\t\t\tEnter genre ")
                    for i in g:
                        if(g[i][1]==genre):
                            print("\n\t\tGenre\tISRC\tSong Name")
                            print(g[i][1],i,g[i][0],sep='\t') 
                            flag=1
                            break
                
                    if(flag==0):
                        print("\n\t\t\tGenre doesn't match our records:/")


    except:
        pass
        f.close()
            
            
def update_all(isrc):
    f=open('data.dat','rb')
    g=open('temp.dat','ab')
    s_name=input("\n\t\t Enter Song Name ")
    g_name=input("\n\t\t Enter Genre of the Song ")
    a_name=input("\n\t\t Enter Artist's Name ")
    y_rl=int(input("\n\t\t Enter Year of Release "))
    tempo=input("\n\t\t Enter Tempo of the Song ")
    streams=int(input("\n\t\t Enter number of streams "))
    a_music[isrc]=[s_name,g_name,a_name,y_rl,tempo,streams]
    pickle.dump(a_music,g)
    os.remove('data.dat')
    os.rename('temp.dat','data.dat')

    f.close()
    g.close()
        
           
def update_records():
    f=open('data.dat','rb')
    g=open('temp.dat','ab')
    flag=0

    try:
        while(True):
            r=pickle.load(f)
            ch=input("\n\t\tDo you want to update all the records (Y/N) ")
            isrc=input("\n\t\t\tPut in the ISRC, for which you want to update records ")
            if(ch.lower()=='y'):
                update_all(isrc)

            else:
                print("\n\t\t\tWhat do you want to update:\n\t1. Song Name\n2. Artist\n3. Year of Release\n4. Tempo\n5. Genre\n6. Streams")
                ch2=int(input("\n\t\t\t\tEnter from the above options "))
        
                for i in r:
                    if(isrc==i):
                        flag=1
                        print("\n\t\tUpdation starting NOW")
                        time.sleep(1.5)   
            
                        if(ch2==1):
                            s_name=input("\t\t\tEnter New Song Name ")
                            a_music[i][0]=s_name
                            pickle.dump(a_music,g)
            
                        elif(ch2==2):
                            artist=input("\t\t\tEnter New Artist Name ")
                            a_music[i][2]=artist
                            pickle.dump(a_music,g)
            
                
                        elif(ch2==3):
                            y_o_r=int(input("\t\t\tEnter New Year of Release "))
                            a_music[i][3]=y_o_r
                            pickle.dump(a_music,g)
            
                        elif(ch2==4):
                            tempo=input("\t\t\tEnter New Tempo ")
                            a_music[i][4]=tempo
                            pickle.dump(a_music,g)
            
                        elif(ch2==5):
                            g_name=input("\t\t\tEnter New Genre ")
                            a_music[i][2]=g_name
                            pickle.dump(a_music,g)
                
                        elif(ch2==6):
                            streams=int(input("\t\t\tEnter New Number of Streams "))
                            a_music[i][5]=streams
                            pickle.dump(a_music,g)
            
                        else:
                            print("\n\t\tYou've entered wrong choice ")
                    else:
                        pickle.dump(r,g)

    except:
        pass
                    
    if(flag==0):
        print("\n\t\t\tISRC doesn't match our records:/")
    else:
        print("\n\t\t\tUpdation Successful!")

    f.close()
    g.close()
    os.remove('data.dat')
    os.rename('temp.dat','data.dat')

def remove_records():
    f=open('data.dat','rb')
    g=open('temp.dat','ab')
    flag=0
    ch=input("\n\t\tEnter ISRC of the record which you wanna delete ")
    try:
        while(True):
            h=pickle.load(f)
            for i in h:
                if(i!=ch):
                    pickle.dump(h,g)
                    break
                else:
                    flag=1
                    
    except:
        pass
    if(flag==0):
        print("\n\t\tIncorrect ISRC entered")
    else:
        print("\n\n\t\tSuccessfully Removed")
        
    f.close()
    g.close()
    os.remove('data.dat')
    os.rename('temp.dat','data.dat')


def choice(ch3):
    if(ch3.lower()=='a'):
        add_data()
    elif(ch3.lower()=='b'):
        view_data()
    elif(ch3.lower()=='c'):
        search()
    elif(ch3.lower()=='d'):
        remove_records()
    elif(ch3.lower()=='e'):
        update_records()
    else:
        print("\n\t\t\t\t\tsorry! wrong choice entered")

