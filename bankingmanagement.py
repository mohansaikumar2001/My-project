
                                            # = # = # = #   Connection through python to mysql   # = # = # = #

import random
import mysql.connector as db
con=db.connect(user='root', password='sai@123', host='localhost', database='Bank')
#print(con)
cursor = con.cursor()

                                                        # # - - = =   BEGINING OF THE PROJECT   = = - - # # 

                    # Admin details interface 

while True:
    print('1.Admin')
    print('2.User')
    print('3.Message')
    print('4.Exit')
    ch = int(input('Enter(user or admin or exit: )'))
    if ch == 1:
        user = input('Enter username: ')
        password = input('Enter password: ')
        if user == 'admin' and password == '2001':
            print('=*=*=*=*=*= Password is correct and Welcome to our bank =*=*=*=*=*=')
        
                    #Users menu interface

            while True:
                print('1. View all users')
                print('2. View complete Account Details of particular User')
                print('3. View complete Transaction of particular User')
                print('4. View complete Transaction of particular Day')
                print('5. Exit')
                option = int(input('Choose your option: '))

                if option == 1:
                    cursor.execute('select * from user2')
                    data = cursor.fetchall()

                    print('= = = = = = = = = = All Users * * * * * * * *')

                    for i in data:
                        print(i)
                        print()

                elif option == 2:
                    account_number = input('Enter account_number: ')
                    cursor.execute('select * from user2 where account_number = %s', (account_number,))
                    data = cursor.fetchall()
                    if not data:
                        print('No user found with this account....')
                    else:
                        for i in data:
                            print(i)
                            print()

                elif option == 3:
                    account_number = input('Enter account_number: ')
                    cursor.execute('select * from transaction1 where account_number = %s', (account_number,))
                    data = cursor.fetchall()
                    if not data:
                        print('No transactions found with this account....')
                    else:
                        for i in data:
                            print(i)
                            print()

                elif option == 4:
                    d = input('Enter the date: ')
                    cursor.execute('select * from transaction1 where date(t_time) = %s', (d,))
                    data = cursor.fetchall()
                    if not data:
                        print('No transactions found on that date....')
                    else:
                        for i in data:
                            a=i[0]
                            am=i[1]
                            t=i[2]
                            t_t=i[3]
                            print(a,'-',am,'-',t,'-',t_t)
                            print(i)
                            print()

                elif option == 5:

                    print('** ** ** **  Returning to main menu  ** ** ** **')
                    break
                else:

                    print('!Invalid choice! **= =** !Try again!')

        else:

            print('!-- Incorrect password --!')

           

                    # User inserting details interface

    elif ch == 2:
        while True:
            print('1.New User')
            print('2.Existing User')
            print('3.Exit')

            print('= = = = = = = = = = = = = = = = = = = = = =')
            fir = int(input('New user or Existing user: '))
            print('= = = = = = = = = = = = = = = = = = = = = =')

            if fir == 3:
                break
            if fir == 1:
                name = input('Enter your name: ')
                while True:
                    mobile_number = input('Enter your mobile number: ')
                    if len(mobile_number)==10 and (mobile_number[0]=='9' or mobile_number[0]=='8' or mobile_number[0]=='7' or mobile_number[0]=='6'):
                        print('valid phone number')
                        break
                    else:
                        print('invalid phone number')

                aadhar_number = str(random.randint(100000000000, 999999999999))
                print('Your aadhaar number is: ', aadhar_number)

                while True:
                    pin_number = input('Enter your pin number: ')
                    if len(pin_number) == 4 or 6:
                        print('valid pin number')
                        break
                    else:
                        print('invalid pin number')
            
                amount = int(input('Enter the amount: '))
                account_number = str(random.randint(100000000000, 999999999999))
                print('Your account number is: ', account_number)
                cursor.execute('''insert into user2(user_name, mobile_number, aadhar_number, pin_number, account_number, amount) values(%s, %s, %s, %s, %s, %s)''',
                (name, mobile_number, aadhar_number, pin_number, account_number, amount))
                con.commit()

                print('- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *')
                print('User registered succesfully')
                print('- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *- *')

            while True:
                account_number = input('Enter account number: ')
                pin_number_login = input('Enter pin_number: ')
                cursor.execute('select account_number, pin_number from user2 where account_number = %s', (account_number,))
                data = cursor.fetchone()
                if data and data[0] == account_number and data[1] == pin_number_login:

                     print('* * * * * * * * * * * * * * * * * * * * * *')
                     print('Login succesfully')
                     print('* * * * * * * * * * * * * * * * * * * * * *')

                     fir = 2
                     break
                else:

                     print('!--- Login again ---!')
                    
                    # Account viewing details interface

            if fir == 2:
                while True:
                    print('1.View account details')
                    print('2.Debit amount')
                    print('3.Credit account')
                    print('4.Pin change')
                    print('5.Statement')
                    print('6.Exit')
                    user_option = int(input("Enter your choice: "))
                            
                            
                    if user_option == 1:
                        account_number = input('Enter your account  number: ')
                        pin_number = input('Enter your pin number: ')
                        cursor.execute('select * from user2 where account_number = %s', (account_number,))
                        user = cursor.fetchone()
                        print('= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =  = ')
                        print(user)
                        print('= = = = = = = = = = = = = = = = = = = = = = = =  = = = = = = = = = = = = = = = = = = = = = = = = = ')


                    if user_option == 2:
                        account_number = input('Enter your account_number: ')
                        pin_number = input('Enter your pin_number: ')
                        cursor.execute('select amount,pin_number from user2 where account_number = %s', (account_number,))
                        data = cursor.fetchone()
                        amount,pin1 = data
                        if pin1 == pin_number:
                            a = int(input('Enter how much amount to withdraw: '))
                            if amount>a:
                                amount = amount-a

                                print('* * * * * * Amount Debited Successfully * * * * * *')

                                cursor.execute('update user2 set amount = %s where account_number = %s', (amount,account_number,))
                                cursor.execute("insert into transaction1 (account_number, amount, type, t_time) values(%s, %s, 'debit', now())", (account_number, amount,))
                                con.commit()
                            else:

                                print('. . . . . . Insuffient balance . . . . . .')
                       

                        cursor.execute('update transaction1 set amount = %s where account_number = %s', (amount,account_number,))

                    if user_option == 3:
                        account_number = input('Enter your account_number: ')
                        pin_number = input('Enter your pin_number: ')
                        cursor.execute('select amount,pin_number from user2 where account_number = %s', (account_number,))
                        data = cursor.fetchone()
                        amount,pin1 = data
                        if pin1 == pin_number:
                                a = int(input('Enter how much amount to credit: '))
                                amount = amount+a

                                print('* * * * * * Amount Credited Successfully * * * * * *')

                                cursor.execute('update user2 set amount = %s where account_number = %s', (amount,account_number,))
                                cursor.execute("insert into transaction1 (account_number, amount, type, t_time) values(%s, %s, 'credit', now())", (account_number, amount,))
                        else:
                                 print('!-- -- Insufficient balance -- --!')
                               
                    if user_option == 4:
                        account_number = input('Enter your account number: ')
                        pin_number = input('Enter your pin number: ')
                        cursor.execute('select pin_number from user2 where accoun_number= %s', (account_number,))
                        data = cursor.fetchone()
                        pin1 = data[0]
                        if pin_number == pin1:
                            pin1 = input('Enter your new pin: ')
                            if len(pin1) == 4:

                                print('*** ***  Pin updated successfully  *** ***')

                                cursor.execute('update user2 set pin_number= %s where account_number= %s', (pin_number,account_number,))
                            else:

                                print('!-  -!You entered wrong pin!-  -!')
                            
                        
                    if user_option == 5:
                        account_number = input('Enter your account number: ')
                        pin_number = input('Enter your pin number: ')
                        cursor.execute('select pin_number from user2 where account_number= %s', (account_number,))
                        data = cursor.fetchone()
                        pin1 = data[0]
                        if pin_number == pin1:
                            cursor.execute('select amount,type,t_time from transaction1 where account_number= %s', (account_number,))
                            s = cursor.fetchall()
                            for i in s:
                                amount = i[0]
                                t = i[1]
                                t_time = i[2]
                                print(amount,'-',t,'-',t_time)
                                print()

                    if user_option == 6:
                        break
               
    elif ch == 3:

         print('****  Thank you** **Visit again   ****')

    else:

        print('= = = =   **Exit from the bank successfully**  = = = = ')
        break


                         # - - # * *   END OF THE PROJECT   * * # - - #

con.close()


                                             






























