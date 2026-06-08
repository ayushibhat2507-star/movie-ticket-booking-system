import random
import mysql.connector as conn
con=conn.connect(host='localhost',user='root',passwd='',database='project')
print("Connected!")
c=con.cursor()
c.execute("SHOW TABLES")
for table in c:
    print(table)
booking_info={}
def book_movies():
    print("Available Movies:")
    print()
    movies()
    print()
    choice()

def choice():
    ch=int(input('''Do you want to
1.Choose genre
2.Book ticket
Enter your choice: '''))
    if ch==1:
        genre()
        print()
        choice()
    if ch==2:
        ticket()
    else:
        print("Invalid Choice")
        choice()
        
def genre():        
    q=("select genre from movies group by genre")
    c.execute(q)
    d=c.fetchall()
    for i in d:
        print(i)
    print()
    g=input("Enter the genre: ")
    v=g,
    Q="select Name from movies where genre=%s"
    c.execute(Q,v)
    D=c.fetchall()
    if len(D)==0:
        print("No movies available for this genre")
    else:
       print("The movies available for this genre are: ",D)

def ticket():
    m=int(input("Enter the movie code for which you want to book tickets: "))
    v=m,
    q="select mcode,count(*) from Lang where mcode=%s"
    c.execute(q,v)
    d=c.fetchall()
    if d[0][0] is None:
        print("No movie available for the given code ")
        ticket()
    if d[0][1]>1:
        print("The given movie is available in the following languages:")
        lang(m)
        l=input("Choose language: ")
        pre(m,l)
    else:
        pree(m)

def pre(m,l):
    v=m,
    q="select Name,rating,genre from movies where mcode=%s"
    c.execute(q,v)
    d=c.fetchall()
    for i in d:
        print("Name: ",i[0])
        print("Rating: ",i[1])
        print("Genre: ",i[2])
    print("Language: ",l)
    book()

def pree(m):
    v=m,
    q="select Name,rating,genre,lang from movies natural join Lang where mcode=%s"
    c.execute(q,v)
    d=c.fetchall()
    for i in d:
        print("Name: ",i[0])
        print("Rating: ",i[1])
        print("Genre: ",i[2])
        print("Language: ",i[3])
    book()
    
def book():
    b=input("Book Tickets? (y/n) ")
    if b.lower()=='y':
        date()
    elif b.lower()=='n':
        print()
        home()
    else:
        print("Enter valid choice")
        book()
    
def date():
    d=input("Do you want to book tickets for today or tomorrow? ")
    if d.lower()=="today":
        mallt()
    elif d.lower()=="tomorrow":
        mallto()
    else:
        print("Enter 'today' or 'tomorrow': ")
        date()

def mallt():
    q="select * from mallt"
    c.execute(q)
    d=c.fetchall()
    for i in d:
        if len(i[1])>23 and len(i[1])<=28 and i[2]=="non-cancellable":
            print(i[0],"\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
        elif len(i[1])>23 and len(i[1])<=28:
            print(i[0],"\t",i[1],"\t\t\t",i[2],"\t\t",i[3])
        elif len(i[1])<23 and i[2]=="non-cancellable":
            print(i[0],"\t",i[1],"\t\t\t\t",i[2],"\t\t\t",i[3])
        elif len(i[1])<23:
            print(i[0],"\t",i[1],"\t\t\t\t",i[2],"\t\t",i[3])
        else:
            print(i[0],"\t",i[1],"\t",i[2],"\t\t\t",i[3])
    print()
    print("These are the available shows for today....")
    z=int(input("Enter your choice: "))
    timet(z)
    
def mallto():
    q="select * from mallto"
    c.execute(q)
    d=c.fetchall()
    for i in d:
        if len(i[1])>20 and len(i[1])<=29:
            print(i[0],"\t",i[1],"\t\t",i[2],"\t",i[3])
        elif len(i[1])<20:
            print(i[0],"\t",i[1],"\t\t\t",i[2],"\t",i[3])
        elif len(i[1])>29 and i[2]=="non-cancellable":
            print(i[0],"\t",i[1],"\t",i[2],"\t\t",i[3])
        else:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
    print()
    print("These are the available shows for tomorrow....")
    z=int(input("Enter your choice:"))
    timeto(z)        
    
def timet(z):
    v=z,
    q="select time from mallt where Mno=%s"
    c.execute(q,v)
    d=c.fetchall()
    for i in d:
        e=str(i[0])
        k=e.split(',')
        if (len(e.split(',')))>1:
            print("Following are the available timings: ")
            print("1.",k[0])
            print("2.",k[1])
            g=int(input("Choose any one: "))
            if g in (1,2):
                seats()
            else:
                print("Enter 1 or 2")
                mallt()
        else:
            print("Following are the available timings: ")
            print(k[0])
            r=input("Continue?....(y/n): ")
            if r.lower()=='y':
                seats()
            elif r.lower()=='n':
                mallt()
            else:
                print("Invalid Choice")
                mallt()

def timeto(z):
    v=z,
    q="select time from mallto where Mno=%s"
    c.execute(q,v)
    d=c.fetchall()
    for i in d:
        e=str(i[0])
        k=e.split(',')
        if len(e.split(','))>1:
            print("Following are the available timings:")
            print("1.",k[0])
            print("2.",k[1])
            g=int(input("Choose any one: "))
            if g in (1,2):
                seats()
            else:
                mallto()
        else:
            print("Following are the timings: ")
            print(k[0])
            r=input("Continue?....(y/n): ")
            if r.lower()=='y':
                seats()
            elif r.lower()=='n':
                mallto()
            else:
                mallto()
                
                
def seats():
    s=int(input("How many seats? (1-10): "))
    disp()
    sc=input('''Choose type of seat: ''')
    price(sc,s)

def disp():
    print()
    print('''Classic: A-F''')
    print()
    print('''Executive: G-N''')
    print()
    print('''Recliner: P''')

Lst=[]
def price(sc,s):
    global Lst
    if sc[0]>='A' and sc[0]<='F':
        for i in range(0,s):
            r=str(random.randint(1,40))
            cs=sc+r
            Lst.append(cs)
        p=180*s
        print("Total price:",p)
        C=input("Continue?...(y/n): ")
        if C.lower()=='y':
            rev(sc,s,p)
        elif C.lower()=='n':
            edit()            
    elif sc[0]>='G' and sc[0]<='N':
        for i in range(0,s):
            r=str(random.randint(1,30))
            cs=sc+r
            Lst.append(cs)
        p=250*s
        print("Total price:",p)
        C=input("Continue?...(y/n): ")
        if C.lower()=='y':
            rev(sc,s,p)
        elif C.lower()=='n':
            edit()
    elif sc[0]=='P':
        for i in range(0,s):
            r=str(random.randint(1,20))
            cs=sc+r
            Lst.append(cs)
        p=300*s
        print("Total price:",p)
        C=input("Continue?...(y/n): ")
        if C.lower()=='y':
            rev(sc,s,p)
        elif C.lower()=='n':
            edit()
    else:
        print("Invalid input")
        disp()
        print("Please enter again ")
        book()
        
def edit():
    print('''Do you want to
1.Edit seats
2.Exit''')
    print()
    ch=int(input("Enter your choice: "))
    if ch==1:
        seats()
    elif ch==2:
        home()
    else:
        print("Invalid Input")
        edit()

def rev(sc,s,p):
    print()
    print("***BOOKING SUMMARY***")
    print(Lst,"(",s,"tickets )","\t","Rs.",p)
    print("Convenience fees:        Rs. 92")
    print("Sub total:               Rs.",(p+92))
    booking_info['sc']=sc
    booking_info['s']=s
    booking_info['p']=p
    paym()

def paym():
    print()
    print('''Do you want to
1.Proceed to pay
2.Prebook your meal''')
    ch=int(input("Enter your choice: "))
    if ch==1:
          pay()
    elif ch==2:
        meal()
    else:
        print("Invalid Choice")
        paym()

def meal():
    print()
    c.execute("select * from meal" )
    d=c.fetchall()
    print("Item Code","\t\t","Item","\t\t\t\t\t\t\t\t\t\t","Price")
    print()
    for i in d:
        if len(i[1])<6:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t\t\t\t\t\t\t",i[2])
        elif len(i[1])>=6 and len(i[1])<14:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t\t\t\t\t\t",i[2])
        elif len(i[1])>=14 and len(i[1])<22:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t\t\t\t\t",i[2])
        elif len(i[1])>22 and len(i[1])<38:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t\t\t",i[2])
        elif len(i[1])==38:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t\t",i[2])
        elif len(i[1])>38 and len(i[1])<=50:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t",i[2])
        elif len(i[1])>50:
            print(i[0],"\t\t\t",i[1],"\t\t",i[2])
    meal_book()
cost=0
def meal_book():
    global cost
    print()
    ch=int(input("Enter Item code: "))
    v=ch,
    c.execute("select Price from meal where No=%s",v)
    d=c.fetchall()
    cost+=int(d[0][0])
    a=int(input('''Do you want to
1.Add more items to your meal
2.proceed
Enter your choice: '''))
    if a==1:
        meal_book()
    elif a==2:
        mbill()
    else:
        print('''Invalid choice
Enter again''')
        meal_book()
            
def mbill():
    print()
    print("***BOOKING SUMMARY***")
    print(Lst,"(",booking_info['s'],"tickets )","\t","Rs.",booking_info['p'])
    print("Food & Beverages:        Rs.",cost)
    print("Convenience fees:        Rs. 92")
    print("Sub total:               Rs.",(booking_info['p']+92+cost))
    final()

def final():
    print('''Do you want to
1.Proceed to pay
2.Exit''')
    ch=int(input("Enter your choice: "))
    if ch==1:
        pay()
    elif ch==2:
        home()
    else:
        print("Invalid choice")
        final()   
    
def pay():
    print("Share your contact details ")
    e=input("Enter your email id: ")
    p=int(input("Enter your mobile no. : "))
    if len(str(p))>10:
        print("Please enter valid mobile number")
        pay()
    print('''Payment Options
1.Credit/Debit card
2.UPI
3.Exit''')
    ch=int(input("Enter your choice: "))
    if ch==1:
        card()
    elif ch==2:
        upi()
    elif ch==3:
        edit()

def card():
    print("Enter your card details")
    cn=input("Enter your card number: ")
    nm=input("Enter the name on card: ")
    ex=input("Enter the expiry(mm/yy): ")
    cvv=input("Enter the CVV: ")
    print("Confirm payment?")
    ch=input("Enter Y/N: ")
    if ch in 'Yy':
        conf()
    elif ch in 'Nn':
        home()
    else:
        print("Invalid input")
        card()

def upi():
    uid=input("Enter UPI  id: ")
    bnk=input("Enter bank: ")
    print("Make payment?")
    ch=input("Enter Y/N: ")
    if ch in 'Yy':
        conf()
    elif ch in 'Nn':
        home()
    else:
        print("Invalid input")
        card()

def conf():
    print("Booking confirmed!!!")
    print("Tickets have been sent to your email id")
    print("Thankyou for using Reel Rush :)")
    home()
    
    
def lang(m):
    v=m,
    q="select lang from Lang natural join movies where mcode=%s"
    c.execute(q,v)
    d=c.fetchall()
    print(d)

def movies():
    c.execute("select * from movies")
    d=c.fetchall()
    print("*"*100)
    print("Movie","\t\t\t\t\t","Genre","\t\t\t\t","Rating","\t","Movie Code")
    print("*"*100)
    for i in d:
        if len(i[0])<=6 and i[1]!="drama":
            print(i[0],"\t\t\t\t\t",i[1],"\t\t\t",i[2],"\t\t",i[3])
        elif len(i[0])<=6 and (i[1]=="drama"):
            print(i[0],"\t\t\t\t\t",i[1],"\t\t\t\t",i[2],"\t\t",i[3])
        elif len(i[0])>=7 and len(i[0])<=14:
            print(i[0],"\t\t\t\t",i[1],"\t\t\t",i[2],"\t\t",i[3])
        elif len(i[0])>=15 and len(i[0])<=22 and (i[1]=="comedy"or i[1]=="fantasy"):
            print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t",i[3])
        elif len(i[0])>=15 and len(i[0])<=22:
            print(i[0],"\t\t\t",i[1],"\t\t\t\t",i[2],"\t\t",i[3])
        elif len(i[0])>22 and len(i[0])<=30:
            print(i[0],"\t\t",i[1],"\t\t\t",i[2],"\t\t",i[3])
        elif len(i[0])>30:
            print(i[0],"\t",i[1],"\t\t\t",i[2],"\t\t",i[3])

L={}
def add_review():
    if len(L)==0:
        print('''No Reviews yet...
Be the first one...''')
    else:
        for i in L.items():
            print(i)
    print()
    y=input('''Add more Reviews?
Enter y/n: ''')
    if y in "Yy":
        print()
        m=input("Enter the movie name: ")
        r=input("Add your Review: ")
        L[m]=r
        print()
        print("Thanks for your Review")
        print()
        home()
    elif y in 'Nn':
        print()
        home()
    else:
        print()
        print("Please enter correctly")
        add_review()
            
def home():    
    a=int(input('''What do you want to do?
1.Book Tickets
2.Add Review
3.Exit

Enter your choice: '''))
    print()
    if a==1:
        book_movies()
    elif a==2:
        add_review()
    elif a==3:
        print("Thankyou...")
        
    else:
        print("Invalid Choice")
        print()
        home()
        
print("WELCOME TO REEL RUSH!!!")
print()
nm=input("Please Enter your name: ")
print()
print('''Welcome''',nm,)


def main():
    try:
        home()
    except:
        print('An error occured....Restarting program')
        print()
        print()
        print()
        home()
main()
