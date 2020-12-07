import mysql.connector as sq
import time
import os
#database password
MySQL_passwd = 'root'
os.system('cls')

#This is to withdawal money

def withdraw():
    mydb = sq.connect(host='localhost', user='root', passwd=f'{MySQL_passwd}', database='public_bank')
    cursor = mydb.cursor()
    os.system('cls')
    print('-'*50)
    print('    <<<    Withdrawal Your Money Here      >>>')
    print('-'*50)
    user = input("User id:")
    passwrd = input("Password:")
    os.system('cls')
    try:
        cursor.execute(f"Select name from Bank1 where user_id='{user}' and Password='{passwrd}'")
        name = cursor.fetchone()
        for x in name:
            name = x
        cursor.execute(f"Select amount from Bank1 where user_id='{user}' and Password='{passwrd}'")
        data = cursor.fetchone()
        for i in data:
            print('-' * 50)
            print(f'    <<<     Welcome {name}      >>>')
            print('-' * 50)
            print('_' * 50)

        print('available balance is :', i)
        balance_withdraw = int(input("Enter Ammount to withdraw: "))

        if balance_withdraw < i and balance_withdraw > 0:
            try:
                new_ammount = i - balance_withdraw

                cursor.execute(f"update bank1 set amount = {new_ammount} where user_id = '{user}'")
                mydb.commit()
                print("Collect Your Money.......,\nYour Avalable balance is ", new_ammount,'\nThankyou.......')
                print('_'*50,)
                print('-'*50)
                x = input()

            except:
                print("Error")
                pass

        elif balance_withdraw > i:
            print("You Don't have sufficient balance !")

        elif balance_withdraw <= 0:
            print("Wrong Ammount !!!")

        else:
            pass

    except:
        print("Wrong input")
        pass

# This to deposit

def Deposit():
    mydb = sq.connect(host='localhost', user='root', passwd=f'{MySQL_passwd}', database='public_bank')
    cursor = mydb.cursor()
    os.system('cls')
    print('-' * 50)
    print('    <<<    Deposit Your Money Here         >>>')
    print('-' * 50)
    user = input("User id:")
    passwrd = input("Password:")
    os.system('cls')
    try:
        cursor.execute(f"Select name from Bank1 where user_id='{user}' and Password='{passwrd}'")
        Name = cursor.fetchone()
        for x in Name:
            name = x
        cursor.execute(f"Select amount from Bank1 where user_id='{user}' and Password='{passwrd}'")
        data = cursor.fetchone()
        for i in data:
            print('-' * 50)
            print(f'    <<<     Welcome {name}      >>>')
            print('-' * 50)
            print('_' * 50)
        print('available balance is :', i)
        balance_diposit = int(input("Enter Ammount to Deposit: "))
        balance = i + balance_diposit

        try:
            cursor.execute(f"update bank1 set amount= {balance} where user_id='{user}' and Password='{passwrd}'")
            data = cursor.fetchone()
            mydb.commit()
            print('_'*50, "\nMoney Deposited.......,\nYour Avalable balance is ", balance, '\nThankyou.......')
            input('press any key...')

        except:
            print("error")

            print(input("Enter any key to exit"), "Byee....")

    except:
        print(input("Enter any key to exit"), "Byee....")
        pass

# This updates your password

def update_password():
    mydb = sq.connect(host='localhost', user='root', passwd=f'{MySQL_passwd}', database='public_bank')
    cursor = mydb.cursor()
    os.system('cls')
    print('-' * 50)
    print('    <<<    Withdrawal Your Money Here      >>>')
    print('-' * 50)
    user = input("User id:")
    passwrd = input("Password:")
    os.system('cls')
    try:
        cursor.execute(f"Select name from Bank1 where user_id='{user}' and Password='{passwrd}'")
        data = cursor.fetchone()
        for name in data:
            print('-' * 50)
            print(f'    <<<     Welcome {name}      >>>')
            print('-' * 50)
            print('_' * 50)
        passwrd1 = input("Enter New Password   : ")
        passwrd2 = input("Confirm Your Password: ")

        if passwrd1 == passwrd2:
            try:
                cursor.execute(f"update Password set Password= '{passwrd1}' where user_id='{user}' and Password='{passwrd}'")
                mydb.commit()
                print("Password Changed Success", input())

            except:
                pass

        else:
            print("password not matches")

    except:
        pass

#For net banking

def net_banking():
    mydb = sq.connect(host='localhost', user='root', passwd=f'{MySQL_passwd}', database='public_bank')
    cursor = mydb.cursor()
    os.system('cls')
    print('-' * 50)
    print('    <<<    Welcome to Public bank    >>>\n    <<<    Net Banking               >>>')
    print('-' * 50)
    user = input("User id:")
    passwrd = input("Password:")
    os.system('cls')
    try:
        cursor.execute(f"Select name from Bank1 where user_id='{user}' and Password='{passwrd}'")
        payer_name = cursor.fetchone()
        for Name in payer_name:
            name = Name
        cursor.execute(f"Select amount from Bank1 where user_id='{user}' and Password='{passwrd}'")
        payer_balance = cursor.fetchone()
        for amount in payer_balance:
            print('-' * 50)
            print(f'    <<<     Welcome {name}      >>>')
            print('-' * 50)
            print('_' * 50)

        print('available balance is :', amount)
        tranfering_user_id = input("Enter paying user_id :")
        balance_transfer = int(input("Enter Ammount to Transfer : "))

        if balance_transfer < amount and balance_transfer > 0:
            try:
                cursor.execute(f"Select amount from Bank1 where user_id='{tranfering_user_id}'")
                data = cursor.fetchone()
                for x in data:
                    paying_user_new_balance = x + balance_transfer
                    cursor.execute(f"update bank1 set amount = {paying_user_new_balance} where user_id = '{tranfering_user_id}'")
                    mydb.commit()
                try:
                    new_ammount = amount - balance_transfer
                    cursor.execute(f"update bank1 set amount = {new_ammount} where user_id = '{user}'")
                    mydb.commit()
                    print()
                    print("Transfering .", end="")
                    for i in range(7):
                        print(".", end="")
                        time.sleep(0.1)
                    print()
                    print("transaction success.......\nYour Avalable balance is ", new_ammount, '\nThankyou.......')
                    print('_' * 50, )
                    print('-' * 50, input())

                except:
                    pass

            except:
                print("Error")
                pass
        elif balance_transfer > amount:
            print("You Don't have sufficient balance !")

        elif balance_transfer <= 0:
            print("Wrong Ammount !!!")

        else:
            pass
    except:
        pass

#This creates new Database in your system

def new_database():
    os.system('cls')
    try:
        mydb = sq.connect(host='localhost', user='root', passwd=f'{MySQL_passwd}', database='public_bank')
        cursor = mydb.cursor()
        main()


    except:
        print('''
                Database Does not exits
                creating Database..................
                ''')
        try:
            mydb = sq.connect(host='localhost', user='root', passwd='root')
            cusor = mydb.cursor()
            cusor.execute("Create database public_bank")
            mydb = sq.connect(host='localhost', user='root', passwd='root', database='public_bank')
            cusor = mydb.cursor()
            sql = (
                "Create table bank1(user_id varchar(20) primary key, name varchar(25) not null, dob char(10),f_name varchar(25) not null,"
                "phone bigint(10) unique, email varchar(30),City char(15),state char(15),Password varchar(15),amount int(9))")
            cusor.execute(sql)
            mydb.commit()
            print('''database created''')
            xyz = input("press a key to continue")
            new_database()

        except:
            print('Database exits')
            os.system('cls')

#This function create new account

def accountant():
    mydb = sq.connect(host='localhost', user='root', passwd=f'{MySQL_passwd}', database='public_bank')
    cursor = mydb.cursor()
    os.system('cls')
    print("_" * 50)
    print('-' * 50)
    print(' ' * 9, '<<<  Create You Account  >>>', ' ' * 10)
    print(' ' * 9, '<<<  Enter Your Details  >>>', ' ' * 10)
    print("_" * 50)
    print('-' * 50)

    user = input("User Name:")
    name = input("Name: ")
    date = input("DOB 'day-month-year': ")
    father = input("Father's Name: ")
    phone = int(input("Phone: "))
    email = input("Email: ")
    city = input("City: ")
    state = input("State: ")
    password = input("Password: ")
    amount = int(input("Amount:"))

    sql = (
        "insert into bank1(user_id,name,dob,f_name,phone,email,city,state,password,amount)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    val = (user, name, date, father, phone, email, city, state, password, amount)

    try:
        cursor.execute(sql, val)
        mydb.commit()
        print("_" * 50)
        print('-' * 50)
        print('=' * 2, '<<<  Thankyou For Creating Your account  >>>', '=' * 2)
        print("_" * 50)
        print('-' * 50, input("Press any key"))
        os.system('cls')
    except:
        print('`' * 50)
        print("!!!!!  Data Invalid\nTry Again")
        xyz=input("Press enter")

def main():
    os.system('cls')
    print('-'*54)
    time.sleep(0.3)
    print('-'*54)
    time.sleep(0.3)
    heading = "Welcome To Public Bank"
    for x in heading:
        print(' ' * 24+str(x) + '\r', end='')
        time.sleep(0.1)
    print('\r', ' ' * 12, end='')
    for x in heading:
        print(str(x), end='')
        time.sleep(0.3)
    print()
    print('-'*54)
    time.sleep(0.3)
    print('-'*54, end='')
    time.sleep(0.3)

    print('''
    =<<<        [1] Open a new Account            >>>=
    =<<<        [2] Withdraw Money                >>>=
    =<<<        [3] Deposit Money                 >>>=
    =<<<        [4] Net Banking                   >>>=
    =<<<        [5] Change Password               >>>=
    =<<<        [6] Exit/Close                    >>>=''')
    print('`'*54)
    print('`'*54)
    option = int(input("Enter your option: "))
    print('`'*54)

    if option == 1:
        accountant()

    elif option == 2:
        withdraw()

    elif option == 3:
        Deposit()

    elif option == 4:
        net_banking()


    elif option == 5:
        update_password()

    else:
        pass


new_database()
