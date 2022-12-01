#using functions, modules & file handling
import time
import license1 as l
import project as pt
import pickle

print("\t               Welcome to Music Licensing Database🎵🎼")
op=''

while(op.lower()!='n'):
    print("\n\t\t\t     ⚡1.Log-in\n\t\t\t     ⚡2.Sign-up ")
    ch=input("\n\t\t\tSelect from the above ")
    if(ch=='1'):
        Id=input("\n\t\t Enter User Id to continue: ")
        Pass=input("\n\t\t Enter password ⚠ ")
        pt.read(Id,Pass)

    elif(ch=='2'):
        l1=input("\n\t\t\t\tDo you want to create a new account? (Y/N) ")
        if(l1.lower()=='y'):
            Id=input("\t\t\tEnter a new User Id ")
            Pass=input("\t\t\tCreate a new password ") 
            pt.write(Id,Pass)
            
        else:
            print("\n\t\t\tTry Again") 
    else:
        print("\n\t\t\tYou've entered wrong choice!") 
        
        
    op=input("\n\t\t\t\tDo you want to \'LOG-IN\' again? (Y or N) ")
print("\n\t\t\t\t\t have a nice day:)")
