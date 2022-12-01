import project as pt

def menu():
    d=''
    while(d.lower()!='n'): 
        print('''\n\n\t\t\tChoose from the below options~\n\t\t\tA. Add Music Data\n\t\t\tB. Display \'ALL\' Data\n\t\t\tC. Search for Music\n\t\t\tD. Remove Records\n\t\t\tE. Update Records''')
        ch=input("\nWhich operation do you wanna perform? ")
        pt.choice(ch)
        
    d=input("\n\t\tDo you want to continue(Y/N)? " )
    print("\n\t\t\t\tthank you for using our services:)")

