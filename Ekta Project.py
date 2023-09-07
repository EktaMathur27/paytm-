import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="olopcs")
mycursor = mydb.cursor()

print(" WELCOME TO PAYTM SYSTEM ")
mycursor.execute("create database if not exists ekta_mathur")
mycursor.execute("use ekta_mathur")
mycursor.execute('''create table if not exists customer_details(Name varchar(15),Address varchar(30),
                    Account_no int Primary key,Balance int(15),mobile_no varchar(20))''')
mycursor.execute('''create table if not exists Wallet(w_id int(15),w_type varchar(10),
                    Account_no int(20),Amount int(20),Date date,
                    Foreign key(Account_no)references customer_details(Account_no))''')

print(" ************** ****E-wallet ****** *******", "\n")


def insert_customer_details():
    name = input("enter the name")
    adr = input("enter the address")
    acc_no = int(input("enter the account no"))
    bal = int(input("enter the balance"))
    mob = input("enter the mobile number")
    sql = "insert into customer_details values(%s,%s,%s,%s,%s)"
    val = (name, adr, acc_no, bal, mob)

    print("-----------Your records are inserted----------")
    mycursor.execute(sql, val)
    mydb.commit()
    
def insert_Wallet():
    wid="select max(w_id) from Wallet;"
    mycursor.execute(wid)
    myresult=mycursor.fetchone()
    if myresult[0]==None:
        wid=1
    else:
        wid=myresult[0]+1
    
    w_id=wid 
    w_type=input("enter the type which you want to dr. or cr.")
    A_no=int(input("enter the account no"))
    Amt=int(input("enter the amount"))
    Date=input("enter the date")
    sql="select Balance from customer_details where Account_no=%s"
    val=(A_no,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchone()

    bal=myresult[0]
    if w_type =='dr':
    	if bal-Amt <1000:
    		print("You have no sufficient balance to dr amount")
    		main()
    	else:
    		amt=bal-Amt
    else:
    	amt=bal+Amt 

    sql="insert into Wallet values(%s,%s,%s,%s,%s)"
    val=(w_id,w_type,A_no,Amt,Date)
    
    mycursor.execute(sql,val)

    sql= 'update customer_details set Balance=%s where Account_no=%s'
    val=(amt,A_no)
    
    mycursor.execute(sql,val)    
    print("-----------Your records are inserted----------")

    mydb.commit()


def update_customer_details():

    acc_no = int(input('enter the account no.'))
    sql = "select * from customer_details where Account_no=%s"
    val = (acc_no,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    name = input('enter the name[o for old]')
    if name == 'o':
        name = myresult[1]
    address = input('enter the address[o for old]')
    if address == 'o':
        address = myresult[2]
    mobile_no = input('enter the mobile no[o for old]')
    if mobile_no == 'o':
        mobile_no = myresult[3]
    bal = int(input('enter the balance [-1 for old value]'))
    if bal == -1:
        bal = myresult[4]
        sql = 'update customer_details set Name=%s,address=%s,Balance=%s,mobile_no=%s where Account_no=%s'
        val = (name,address,bal,acc_no,mobile_no)
        print ("------------Your records are updated-----------")
        mycursor.execute(sql, val)
        mydb.commit()
def update_Wallet():
    w_id = int(input('enter the Wallet id '))
    sql = 'select*from Wallet where w_id=%s'
    val = (w_id,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchone()
    w_type = input('enter the Wallet type you want to dr or cr[o for old]')
    if w_type == "o":
        w_type = myresult[1]
    Account_no = input('enter the account number[o for old]')
    if Account_no == "o":
        Account_no = myresult[2]
    Amount = input('enter the amount[o for old]')
    if Amount == "o":
        Amount = myresult[3]
    Date = input('enter the date[o for old]')
    if Date =="o" :
        Date = myresult[4]
    sql = 'update Wallet set w_type=%s,Account_no=%s,Amount=%s,Date=%s where w_id=%s'
    val = (w_type, Account_no, Amount, Date, w_id)
    print("------------Your records are updated-----------")
    mycursor.execute(sql, val)
    mydb.commit()

def delete_customer_details():
    Account_no = int(input('enter the Account number to be deleted'))
    sql = 'delete from customer_details where Account_no=%s'
    val = (Account_no,)
    print("-----------Your record are deleted-------------")
    mycursor.execute(sql, val)
    mydb.commit()

def delete_Wallet():
    Account_no = int(input('enter the Account number to be deleted'))
    sql = 'delete from Wallet where Account_no=%s'
    val = (Account_no,)
    print("-----------Your record are deleted-------------")
    mycursor.execute(sql, val)
    mydb.commit()

def displayall_customer_details():
    mycursor.execute("select*from customer_details")
    myresult=mycursor.fetchall()
    print('|','-'*70,'|')
    print('|   Name    |       Address      | Account_no |   Balance   |   Mobile   |')
    print('|','-'*70,'|')
    for x in myresult:
        print("|{0:11}|{1:20}|{2:12}|{3:13}|{4:12}|".format(x[0],x[1],x[2],x[3],x[4]))
    print('|','-'*70,'|','\n')   	

def displayall_Wallet():
    mycursor.execute('select*from Wallet')
    myresult = mycursor.fetchall()
    print('|','-'*57,'|')
    print('|  W_Id  |    W_type    | Accont_no |   Amount   |   Date   |')
    print('|','-'*57,'|')
    for x in myresult:
        print("|{0:8}|{1:14}|{2:11}|{3:12}|{4}|".format(x[0],x[1],x[2],x[3],x[4]))
    print('|','-'*57,'|','\n') 

def displayspecific_user_info():
    Account_no=int(input("enter the account no to be display"))
    sql='select name,address,balance,mobile_no from customer_details where Account_no=%s'
    val=(Account_no,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchone()
    x=myresult
    print('---------------------------') 
    print("Name      : ",x[0])
    print("Address   : ",x[1])
    print("Balance   : ",x[2])
    print("mobile_no : ",x[3])
    print('---------------------------')
    print('_________________________________________') 

def displayspecific_Wallet():
    Account_no = int(input('enter the account no to be displayed'))
    sql = 'select w_id,w_type,Amount,Date,Name from Wallet t,  customer_details a where t.Account_no=a.Account_no and a.Account_no=%s'
    val = (Account_no,)
    mycursor.execute(sql, val)
    myresult=mycursor.fetchone()
    x=myresult
    print('---------------------------') 
    print("'w_id  : ",x[0])
    print("w_type : ",x[1])
    print("Amount : ",x[2])
    print(" Date  : ",x[3])
    print("Name   : ",x[4])
    print('---------------------------')
    print('_________________________________________') 
    



def login():
    print ('|****************************************|')
    user_id = input(' |Enter your user id : ')
    password = input(' |Enter your Password : ')
    print (' | |')
    print (' | |')
    print (' | |')
    if user_id != 'olopcs':
        print (' |Invalid Credentials. Please try again.')
    elif password != 'olopcs':
        print ('|Invalid Credentials. Please try again. ')
        exit()
    else:
        print (' | |')
        print ('|**YOU HAVE SUCCESSFULLY ENTERED IN YOU WALLET**|', )
        print ('|*************************************************|', '\n')


login()

def main_menu():
 print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
 print("|                           PAYTM WALLET                     |")
 print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
 print("|     Customer Information     |       Wallet Operations     |")
 print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
 print("| 1.New Customer               | 11.Create new Wallet        |")
 print("| 2.Update Customer            | 12.Set Transaction          |")
 print("| 3.Remove Customer            | 13.Remove Transaction       |") 
 print("| 4.View all Customer          | 14.View all Transaction     |")
 print("| 5.View Specific Customer     | 15.View specific Transaction|")
 print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
 print("|                       0. To Exit                           |")
 print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|") 

def main():
 while True:
      main_menu()
      choice=int(input("enter the choice:")) 
      print("===============================================")
      if choice==1:
         insert_customer_details()
         
      elif choice==11:
        insert_Wallet()
        
      if choice==2:
        update_customer_details()
        
      elif choice==12:
        update_Wallet()
        
      if choice==3:
        delete_customer_details()
        
      elif choice==13:
        delete_Wallet()
        
      if choice==4: 
        displayall_customer_details()
        
      elif choice==14:
        displayall_Wallet()
        
      if choice==5:
        displayspecific_user_info()
        
      elif choice==15:
        displayspecific_Wallet()

      if choice==0:
        exit() 

main()
